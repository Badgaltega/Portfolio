from django.shortcuts import render

def home(request):
    context = {}
    return render(request, "resume/index.html", context)