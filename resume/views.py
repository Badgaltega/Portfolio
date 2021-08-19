from django.shortcuts import render, redirect
from django.contrib import messages
from resume.models import Message


def home(request):
    context = {}
    return render(request, "resume/index.html", context)


def send_message(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    subject =  request.POST.get("subject")
    message = request.POST.get("message")

    save_message = Message(
        name=name, email=email, subject=subject, message=message
    )
    save_message.save()
    messages.success(request, "Yayy! Your message has been submitted.")

    return redirect("resume:home")