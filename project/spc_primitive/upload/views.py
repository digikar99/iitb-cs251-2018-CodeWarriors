from django.shortcuts import render
from django.conf import settings

# Create your views here.
def upload(request):
    return render(request, "home.html")
