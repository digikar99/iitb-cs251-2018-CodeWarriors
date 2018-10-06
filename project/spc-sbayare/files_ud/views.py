from django.shortcuts import render
from django.http import HttpResponse
import os
from django.utils.encoding import smart_str
# Create your views here.

def index(request): # [1]
    '''
    Sends the contents of file_name as response
    '''
    file_name = 'in.txt'
    response = HttpResponse(content_type='application/force-download')
    # There are some limitations to smart_str
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name)
    response['X-Sendfile'] = smart_str(file_name)
    # It's usually a good idea to set the 'Content-Length' header too.
    # You can also set any other required headers: Cache-Control, etc.
    return response


'''
References:

1.  https://stackoverflow.com/questions/1156246/having-django-serve-downloadable-files

''' 
