from django.shortcuts import render
from django import forms
from django.middleware import csrf
from django.views import generic
from . import models
from django.shortcuts import redirect
from django.contrib.auth.models import User

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = models.File
        fields = ['user_name_path', 'file_data',
                  'last_update_time', 'file_type', 'md5sum']
        
class UploadFile(generic.CreateView):
    template_name='upload_file/file_upload.html'
    form_class=UploadFileForm
    success_url = '/home'
    # def dispatch(self, *args, **kwargs):
    #     return super(UploadFile, self).dispatch(*args, **kwargs)

    # def form_valid(self, form):
    #     obj = form.save(commit=False)
    #     obj.owner = self.request.user
    #     obj.save()
    #     return redirect(('/home'))
