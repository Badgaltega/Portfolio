from django.urls import path
from resume import views

app_name = "resume"

urlpatterns = [
    path("", views.home, name="home")
]