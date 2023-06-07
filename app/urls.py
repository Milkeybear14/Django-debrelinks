from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("add",views.add,name="add"),
    path("register",views.register,name="register"),
    path("login",views.login,name="login"),
    path("logout",views.logout,name="logout")
]