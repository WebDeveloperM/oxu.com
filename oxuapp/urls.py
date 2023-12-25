from django.urls import path
from oxuapp.views import (
    home,
    info_user,
    acceptance,
    form_data,
    contract,
    download_contract,
    download_pdf,
)

urlpatterns = [
    path("", home, name="home"),
    path("info_user/", info_user, name="info_user"),
    path("acceptance/", acceptance, name="acceptance"),
    path("form-data/<str:phone>", form_data, name="form-data"),
    path("contract", contract, name="contract"),
    path("download-contract", download_contract, name="download-contract"),
    path("pdf_download/<str:phone>", download_pdf, name="pdf_download"),
]
