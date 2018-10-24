from django.db import models
# Create your models here.

class Directory(models.Model):
    parent=models.IntegerField(blank=True)
    name= models.TextField(blank=True)
    path = models.TextField(blank=True)

class File(models.Model):
    parent = models.IntegerField(blank=True)
    name = models.TextField(blank=True)
    path = models.TextField(blank=True)
    file_data=models.BinaryField(blank=True)

# Although you might think about storing files in the database, consider that it is bad design in 99% of the cases.
# This field is not a replacement for proper static files handling
