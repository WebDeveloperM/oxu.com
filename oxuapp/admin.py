from django.contrib import admin
from oxuapp.models import Info, Announcement, Direction, Support, Contract

# Register your models here.


@admin.register(Info)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ["title", "count"]
    fields = ["title", "count"]



@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ["name", "surename", "phone", "payment_check", "is_payment"]
admin.site.register(Announcement)
admin.site.register(Direction)
admin.site.register(Support)
