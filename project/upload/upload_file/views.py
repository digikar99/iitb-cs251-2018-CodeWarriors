from django.shortcuts import render
from django.http import HttpResponse
import json
from django.http import StreamingHttpResponse

def index(request):
    if request.method=='POST':
        json_data=json.loads(request.body.decode('utf-8'))
        return HttpResponse('The following data was recieved by POST:\n'+str(json_data)+'\n')
    response = HttpResponse('it was GET request')
    response.set_cookie('csrftoken', 'valid')
    return response

# Create your views here.
# def index(request):
#     return HttpResponse("Hello, world.")
