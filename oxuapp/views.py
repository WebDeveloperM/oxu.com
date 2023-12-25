from django.shortcuts import render, redirect
from oxuapp.models import Info, Announcement, Direction, Support, Contract
from django.contrib import messages
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.


def home(request):
    infos = Info.objects.all()
    announcements = Announcement.objects.all()
    directions = Direction.objects.all()

    return render(
        request,
        "home.html",
        {"infos": infos, "announcements": announcements, "directions": directions},
    )


def info_user(request):
    firstname = request.POST.get("firstname")
    surename = request.POST.get("surename")
    father_name = request.POST.get("father_name")
    phone = request.POST.get("phone")
    direction = Direction.objects.filter(title=request.POST.get("direction")).first()

    if not phone or len(phone) != 19:
        messages.error(request, "Bunday telefon raqam mavjud emas")
        return redirect("home")

    if request.method == "POST":
        contract = Support.objects.create(
            name=firstname,
            surename=surename,
            father_name=father_name,
            phone=phone,
            direction=direction,
        )
        messages.success(request, "Sizning ma`lumotlaringiz qabul qilindi")
        return redirect("home")
    return redirect("home")


def acceptance(request):
    phone = request.POST.get("phone")
    if request.method == "POST":
        print(phone, "--------------------")
        contract = Contract.objects.filter(phone=phone).last()
        
        if not phone or len(phone)!=19:
            messages.error(request, "Bunday telefon raqam mavjud emas!")
            return redirect("acceptance")

        if contract and contract.payment_check and not contract.is_payment:
            messages.warning(request, "Ma`lumotlar tasdiqlanmagan. Kuting")
            return redirect("acceptance")

        if contract and contract.is_payment:
            messages.success(request, "Bu telefon raqamda aktive shartnoma mavjud")
            return redirect("acceptance")
        return redirect("form-data", phone)
    return render(request, "acceptance.html")


def form_data(request, phone):
    directions = Direction.objects.all()
    return render(request, "form_data.html", {"directions": directions, "phone": phone})


def contract(request):
    firstname = request.POST.get("firstname")
    surename = request.POST.get("surename")
    father_name = request.POST.get("father_name")
    second_phone = request.POST.get("second_phone")
    phone = request.POST.get("first_phone")
    age = request.POST.get("age")
    stady_lang = request.POST.get("stady_lang")
    contract_type = request.POST.get("contract_type")
    stady_type = request.POST.get("stady_type")
    education_form = request.POST.get("education_form")
    direction = Direction.objects.filter(title=request.POST.get("direction")).first()

    if request.method == "POST":
        contract = Contract.objects.create(
            name=firstname,
            surename=surename,
            father_name=father_name,
            phone=phone,
            second_phone=second_phone,
            age=age,
            contract_type=contract_type,
            stady_lang=stady_lang,
            stady_type=stady_type,
            education_form=education_form,
            direction=direction,
        )
        return redirect("home")
    return redirect("home")


def download_contract(request):
    phone = request.POST.get("phone")
    if request.method == "POST":
        contract = Contract.objects.filter(phone=phone).last()
        if not contract:
            messages.error(request, "Telfon raqam ro`yhatdan o`tmagan")
            return redirect("download-contract")
        if contract and contract.payment_check and not contract.is_payment:
            messages.warning(request, "Ma`lumotlar tasdiqlanmagan. Kuting")
            return redirect("download-contract")

        if contract and contract.is_payment:
            return redirect("pdf_download", phone)
            pass
        return redirect("download-contract")

    return render(request, "download_contract.html")


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type="application/pdf")
    return None


def download_pdf(request, phone):
    data = Contract.objects.filter(phone=phone).last()

    print(data.__dict__)
    if not data:
        return redirect("home")
    pdf = render_to_pdf("contract.html", data.__dict__)

    response = HttpResponse(pdf, content_type="application/pdf")
    filename = "Shartnoma_%s.pdf" % ("12341231")
    content = "attachment; filename=%s" % (filename)
    response["Content-Disposition"] = content
    return response
