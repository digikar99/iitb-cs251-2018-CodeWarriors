from django.shortcuts import render
from django import forms
from django.middleware import csrf
from django.views import generic
from upload_file.models import File
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.core.exceptions import ObjectDoesNotExist

def getChildrenOfFolder(fold_name):
    # check for user.id
    l = File.objects.filter(name_path__startswith=fold_name)
    # and we already know that fold_name ends in '/'

    # create {name: type} pairs for easy parsing in webclient
    print('========================================')
    # print(l)
    name_type = dict()
    for f in l:
        f1 = f.name_path.split(fold_name)[1]
        # this, basically, strips fold_name from the beginning of f
        if '/' in f1:
            # this is a directory
            name_type[f1.split('/')[0]] = 'dir'
        else:
            name_type[f1] = 'file'

    return name_type

def getChildrenOfRootFolder():
    # check for user.id
    l = File.objects.all()
    name_type = dict()
    for f in l:
        f1 = f.name_path
        # this, basically, strips fold_name from the beginning of f
        if '/' in f1:
            # this is a directory
            name_type[f1.split('/')[0]] = 'dir'
        else:
            name_type[f1] = 'file'

    return name_type

def getContents(request, file_path=None):
    if (request.user.is_authenticated):
        # also check if the user.id matches with the owner field of
        # the corresponding file in the database
        #f = File.objects.filter(name_path__startswith=file_path)
        if file_path is None:
            l = getChildrenOfRootFolder()
            return JsonResponse(l)
        elif (file_path.endswith('/')):
            # then this is possibly a directory
            l = getChildrenOfFolder(file_path)
            return JsonResponse(l)
        else:
            f = File.objects.filter(name_path = file_path);
            if len(f) == 0:
                return HttpResponseNotFound()
            else:
                return HttpResponse(f[0].file_data)
    else:
        return HttpResponseForbidden()

# Create your views here.
