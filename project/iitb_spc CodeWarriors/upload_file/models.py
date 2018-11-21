from django.db import models
from django.conf import settings
# Create your models here.

class Directory(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE, )
    parent=models.IntegerField(blank=True)
    name= models.TextField(blank=True)
    path = models.TextField(blank=True)

class File(models.Model):
    #owner = models.ForeignKey(settings.AUTH_USER_MODEL,
    #                          on_delete=models.CASCADE,)
    #parent = models.IntegerField(blank=True)
    name_path = models.TextField(blank=True, null=True)
    file_data=models.TextField(blank=True, null=True)
    last_update_time = models.IntegerField(blank=True, null=True)
    file_type=models.TextField(blank=True, null=True)
    part_no=models.IntegerField(blank=True, null=True)
    md5sum=models.TextField(blank=True, null=True)
# Although you might think about storing files in the database, consider that it is bad design in 99% of the cases.
# This field is not a replacement for proper static files handling
