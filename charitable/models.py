from django.db import models
from  cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.contrib.postgres.fields import RangeField
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
# Create your models here.



class Requests(models.Model):
    fin_statements = models.FileField(upload_to='documents')
    reports = models.FileField(upload_to='documents')
    amount_range = models.IntegerField(default=0,blank=True, null=True)
    verification = models.BooleanField()


class User(AbstractUser):
    is_administrator=models.BooleanField('Is admin', default=False)
    is_NonGo= models.BooleanField('Is Ngo', default=False)
    is_Don=models.BooleanField('Is Donor', default=False)

 
    def __str__(self):
        return self.username

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Administrator(models.Model):
    user = models.OneToOneField(User, related_name="admin", on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, null=True, blank=True)
    password = models.CharField(max_length=243, null=True, blank= True)

    def __str__(self):
        return self.user.username


class NonGo(models.Model):
    user = models.OneToOneField(User, related_name="ngo", on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    password = models.CharField(max_length=243, null=True, blank= True)
    

    def __str__(self):
        return self.company_name

class Don(models.Model):
    user = models.OneToOneField(User, related_name="donor", on_delete=models.CASCADE)
    Don_name = models.CharField(max_length=254, null=True)
    contact = models.IntegerField(default=0,blank=True, null=True)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=243, null=True, blank= True)
    
    def __str__(self):
        return self.Don_name


