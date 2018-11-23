from django.shortcuts import render
from upload_file.models import File
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
from .models import UserSession

def getChildrenOfFolder(fold_name):
    # check for user.id
    l = File.objects.filter(user_name_path__startswith=fold_name)
    # and we already know that fold_name ends in '/'

    # create {name: type} pairs for easy parsing in webclient
    # print('========================================')
    # print(l)
    name_type = dict()
    for f in l:
        f1 = f.user_name_path.split(fold_name)[1]
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
        f1 = f.user_name_path
        # this, basically, strips fold_name from the beginning of f
        if '/' in f1:
            # this is a directory
            name_type[f1.split('/')[0]] = 'dir'
        else:
            name_type[f1] = 'file'

    return name_type

def getContents(request, file_path=None):
    if file_path is None:
        return HttpResponseForbidden()
    elif (request.user.is_authenticated
        and request.user.username == file_path.split('/')[0]):
        Session=UserSession.create(request)
        prev_Session=UserSession.objects.filter(username = request.user)
        if not prev_Session:
            Session.save()
        else:
            time_diff = Session.ip or Session.time - prev_Session[0].time
            if prev_Session[0].ip == time_diff.timediff.total_seconds() > 15*60:
                prev_Session.delete()
                Session.save()
            else:
                return HttpResponseForbidden()
        if file_path is None:
            l = getChildrenOfRootFolder(request.user.username+'/')
            prev_Session = UserSession.objects.filter(username=request.user)
            prev_Session.delete()
            return JsonResponse(l)
        elif (file_path.endswith('/')):
            # then this is possibly a directory
            l = getChildrenOfFolder(file_path)
            prev_Session = UserSession.objects.filter(username=request.user)
            prev_Session.delete()
            return JsonResponse(l)
        else:
            f = File.objects.filter(user_name_path = file_path);
            if len(f) == 0:
                prev_Session = UserSession.objects.filter(username=request.user)
                prev_Session.delete()
                return HttpResponseNotFound()
            else:
                temp_file_data=f[0].file_data
                prev_Session = UserSession.objects.filter(username=request.user)
                prev_Session.delete()
                return HttpResponse(temp_file_data)
    else:
        return HttpResponseForbidden()

def getMd5sum(request, file_path):
    if (request.user.is_authenticated
            and request.user.username == file_path.split('/')[0]):
        return HttpResponse(File.objects.get(user_name_path=file_path).md5sum)
    else:
        return HttpResponseForbidden()


def getLastUpdateTime(request, file_path):
    if (request.user.is_authenticated
            and request.user.username == file_path.split('/')[0]):
        return HttpResponse(File.objects.get(user_name_path=file_path).last_update_time)
    else:
        return HttpResponseForbidden()


def getFileType(request, file_path):
    if (request.user.is_authenticated
            and request.user.username == file_path.split('/')[0]):
        return HttpResponse(File.objects.get(user_name_path=file_path).file_type)
    else:
        return HttpResponseForbidden()


def getAllFiles(request, file_path=None):
    if file_path is None:
        return HttpResponseForbidden()
    elif (request.user.is_authenticated
          and request.user.username == file_path.split('/')[0]):
        if (file_path.endswith('/')):
            dic = dict()
            l = File.objects.filter(user_name_path__startswith=file_path)
            for f in l:
                dic[f.user_name_path] = ""
            return JsonResponse(dic)
            # return HttpResponse('\n'.join(l)) # html ignores new lines
        else:
            return HttpResponseForbidden()
    else:
        return HttpResponseForbidden()


