from django.urls import path
from user_app.api.views import obtain_auth_token

urlpatterns = [
    path("login/", obtain_auth_token, name="login"),
]
