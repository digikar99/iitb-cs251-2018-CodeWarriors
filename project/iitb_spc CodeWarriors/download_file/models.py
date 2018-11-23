from django.db import models
from django.conf import settings
from datetime import datetime
# Create your models here.

class UserSession(models.Model):
    username = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
    )

    string_date=models.CharField(max_length=20)
    ip = models.CharField(max_length=64)

    @classmethod
    def create(cls, request):
        return cls(username = request.user, string_date = str(datetime.now()),ip = get_client_ip(request))

    # def __init__(self,request, *args, **kwargs):
    #     super(models.Model, self).__init__(self, *args, **kwargs)
    #     username = request.user
    #     ip = self.get_client_ip(request)
    #     time = datetime.datetime.now()
    def __str__(self):
        a=(str(self.username),str(self.ip),str(self.string_date))
        return str(a)

    def get_time(self):
        return datetime.strptime(str(self.string_date), "%Y-%m-%d %H:%M:%S.%f")


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip