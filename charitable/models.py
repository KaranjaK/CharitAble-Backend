from django.db import models
from django.contrib.auth.models import AbstractUser

#creating models

class User(AbstractUser):
    is_admin=models.BooleanField('Is admin', default=False)
    is_Ngo= models.BooleanField('Is Ngo', default=False)
    is_Donor=models.BooleanField('Is Donor', default=False)