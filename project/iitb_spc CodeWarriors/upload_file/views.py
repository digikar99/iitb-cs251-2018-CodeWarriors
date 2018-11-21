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

    def dispatch(self, *args, **kwargs):
        return super(UploadFile, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner = self.request.user
        obj.save()
        return redirect(('/home'))

