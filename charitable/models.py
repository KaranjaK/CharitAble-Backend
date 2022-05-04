from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
#creating models

class User(AbstractUser):
    is_admin=models.BooleanField('Is admin', default=False)
    is_Ngo= models.BooleanField('Is Ngo', default=False)
    is_Donor=models.BooleanField('Is Donor', default=False)

    def __str__(self):
        return self.username

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class admin(models.Model):
    user = models.OneToOneField(User, related_name="admin", on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, null=True, blank=True)
    password = models.CharField(max_length=243, null=True, blank= True)

    def __str__(self):
        return self.user.username


class Ngo(models.Model):
    user = models.OneToOneField(User, related_name="ngo", on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    password = models.CharField(max_length=243, null=True, blank= True)
    

    def __str__(self):
        return self.company_name

class Donor(models.Model):
    user = models.OneToOneField(User, related_name="donor", on_delete=models.CASCADE)
    Don_name = models.CharField(max_length=254, null=True)
    contact = models.IntegerField(default=0,blank=True, null=True)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=243, null=True, blank= True)
    
    def __str__(self):
        return self.Don_name

