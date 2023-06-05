from django.urls import path
from usersapp import views

# Template tagging
app_name = "usersapp"
# this app naem iis used in relative_url template to link to other.html

urlpatterns = [
    path("login/", views.user_login, name="user_login"),
    path("register/", views.register, name="register"),
]
