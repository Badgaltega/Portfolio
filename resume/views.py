from django.shortcuts import render, redirect
from django.contrib import messages
from resume.models import Message


def home(request):
    context = {}
    return render(request, "resume/index.html", context)


def send_message(request):

    # Gets value from the form and saves them to their respective variable
    name = request.POST.get("name")
    email = request.POST.get("email")
    subject =  request.POST.get("subject")
    message = request.POST.get("message")

    # Creates a variable named save_message and instantiate the Message model class to it
    save_message = Message(
        name=name, email=email, subject=subject, message=message
    )

    # Saves the data that will be gotten from the form
    save_message.save()
    messages.success(request, "Yayy! Your message has been submitted.")

    return redirect("resume:home")