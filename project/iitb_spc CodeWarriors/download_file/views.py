from django.shortcuts import render
from django import forms
from django.middleware import csrf
from django.views import generic
from upload_file.models import File
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseForbidden

def getContents(request, file_path):
    if (request.user.is_authenticated):
        # also check if the user.id matches with the owner field of
        # the corresponding file in the database
        print("Sending data of " + file_path)
        f = File.objects.filter(name_path=file_path)[0]        
        return HttpResponse(f.file_data)
    else:
        return HttpResponseForbidden()

# Create your views here.
