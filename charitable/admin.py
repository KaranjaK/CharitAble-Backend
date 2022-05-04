from django.contrib import admin
from .models import User, Donor, Ngo, Admin

# Register your models here.
admin.site.register(User)
admin.site.register(Donor)
admin.site.register(Ngo)
admin.site.register(Admin)
