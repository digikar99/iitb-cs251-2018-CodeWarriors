from django.shortcuts import render
from django import forms
from django.middleware import csrf
from django.views import generic
from . import models

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = models.File
        # fields = [
        #     model.name_path,
        #     model.last_update_time,
        #     model.file_type,
        #     model.md5sum
        # ]
        fields = ['name_path', 'file_data',
                  'last_update_time', 'file_type',
                  'md5sum']
        # fields = '__all__'
    # last_update_time = forms.IntegerField(
    #     help_text="Enter last update time as a unix (integer) timestamp",
    #     required=True)

class UploadFile(generic.CreateView):
    template_name='upload_file/file_upload.html'
    form_class=UploadFileForm
    success_url = '/home' 
    
