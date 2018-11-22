from django.middleware import csrf
from upload_file.models import File
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseForbidden

def deleteContents(request,file_path):
    # this is called only if such a file (and definitely not a folder) exists
    if (request.user.is_authenticated
        and request.user.username == file_path.split('/')[0]):
        File.objects.get(user_name_path=file_path).delete()
        return HttpResponse('deleted')
    else:
        return HttpResponseForbidden()



