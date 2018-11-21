from django.shortcuts import render
from django.http import HttpResponse
import json
from django.template import loader
from server_side.models import Directory,File
from django.http import StreamingHttpResponse
from django.shortcuts import render
from django import forms
from django.middleware import csrf

# def index(request):
#     a=csrf.get_token(request)
#     if request.method=='POST':
#         json_data=json.loads(request.body.decode('utf-8'))
#         current_user=request.user
#         flag="fail"
#         if current_user.is_authenticated:
#             flag="sucess...\n" + " current user = " + str(current_user.username) + "\nuser-id=" + str(current_user.id)
#             a=File(owner=current_user ,file_data=json_data['content'].encode())
#         return HttpResponse(flag + ' : The following data was recieved by POST:\n'+str(json_data)+'\n')
#     response = HttpResponse('it was GET request')
#     response.set_cookie('csrftoken', 'valid')
#     return response


def index(request):
    template = loader.get_template('upload_file/file_upload.html')
    return HttpResponse(template.render())


class file_form(forms.Form):
    file=forms.FileField()
    name=forms.CharField(widget=forms.Textarea)


def file_upload(request):
    if request.method == 'POST':
        form=file_form(request.POST)
        if form.is_valid():
            data = request.POST.copy()
            path = data.get('filename')
            content = data.get('filecontent')
    return render(request, 'upload_file/file_upload.html')