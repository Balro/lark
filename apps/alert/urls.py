from django.urls import path
from . import views

app_name = "alert"
urlpatterns = [
    path("ding", views.ding, name="ding"),
    path("phone", views.phone, name="phone"),
    path("mail", views.mail, name="mail"),
]
