from django.db import models
from  cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.contrib.postgres.fields import RangeField

# Create your models here.
class NGO(models.Model):
    name = models.TextField(max_length=50)
    logo = CloudinaryField('images', null=True)
    category = models.TextField()
    description = models.TextField(max_length=200)
    web_link = models.URLField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project')
    contact = models.IntegerField(default=0,blank=True, null=True)
    email = models.EmailField(max_length=100, null=True)
    location = models.CharField(max_length=100)


class Donor(models.Model):
    name = models.TextField()
    logo = CloudinaryField('images', null=True)
    type = models.BooleanField()
    web_link = models.URLField(max_length=300)
    contact = models.IntegerField(default=0,blank=True, null=True)
    email = models.EmailField(max_length=100, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project')
    location = models.CharField(max_length=100)

class Requests(models.Model):
    fin_statements = models.FileField(upload_to='documents/%Y/%m/%d')
    reports = models.FileField(upload_to='documents')
    amount_range = RangeField()




class Admin(models.Model):
    username = models.TextField()
    requests = models.ForeignKey(Requests, on_delete=models.CASCADE, related_name='requests')