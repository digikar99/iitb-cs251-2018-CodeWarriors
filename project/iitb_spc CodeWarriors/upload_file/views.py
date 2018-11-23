from django.shortcuts import render
from django import forms
from django.middleware import csrf
from django.views import generic
from . import models
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseForbidden
from download_file.models import UserSession

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

    def form_valid(self, form):
        obj = form.save(commit=False)
        if obj.user_name_path.split('/')[0] == self.request.user.username:
            Session = UserSession.create(self.request)
            prev_Session = UserSession.objects.filter(username=self.request.user)
            if not prev_Session:
                Session.save()
            else:
                time_diff = Session.get_time() - prev_Session[0].get_time()
                if time_diff.total_seconds() > 15 * 60 or Session.ip == prev_Session[0].ip:
                    a=models.File.objects.filter(user_name_path = obj.user_name_path)
                    a.delete()
                else:
                    return HttpResponseForbidden()
            obj.save()
        else:
            return HttpResponseForbidden()
        super(UploadFile, self).form_valid(form)
        return redirect(('/download_file/sucess/'))
