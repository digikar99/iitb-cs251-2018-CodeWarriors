from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.


class File(models.Model):
    user_name_path = models.CharField(max_length=1023,primary_key=True)
    file_data=models.TextField(blank=True, null=True)
    last_update_time = models.IntegerField()
    file_type=models.TextField(blank=True, null=True)
    # part_no=models.IntegerField(blank=True, null=True) # implement for block level encryption
    md5sum=models.TextField()

    def __str__(self):
        r=(self.user_name_path)
        return str(r)

# Although you might think about storing files in the database, consider that it is bad design in 99% of the cases.
# This field is not a replacement for proper static files handling
