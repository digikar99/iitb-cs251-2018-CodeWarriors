from django.shortcuts import render
from django import forms
from django.middleware import csrf
from django.views import generic
from . import models
from django.contrib.auth.models import User

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = models.File
        fields = ['name_path', 'file_data',
                  'last_update_time', 'md5sum']
    # def save(self, user):
    #     obj = super().save(commit = False)
    #     obj.owner = user
    #     obj.save()
    #     return obj

class UploadFile(generic.CreateView):
    template_name='upload_file/file_upload.html'
    form_class=UploadFileForm # (initial={'owner':request.user.id})
    success_url = '/home'
    from django import forms

    
