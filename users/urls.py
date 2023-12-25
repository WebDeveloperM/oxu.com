from django.urls import path
from users.views import signup

urlpatterns = [
    path("", signup, name="signup")
]