from django.urls import path
from user_app.api.views import obtain_auth_token, registration_view

urlpatterns = [
    path("login/", obtain_auth_token, name="login"),
    path("register/", registration_view, name="register"),
]
