from django.contrib import admin
from .models import User, Don, NonGo, Administrator

from charitable.models import NGO, Donor, Requests,Admin

# Register your models here.
admin.site.register(User)
admin.site.register(Don)
admin.site.register(NonGo)
admin.site.register(Administrator)
admin.site.register(NGO)
admin.site.register(Donor)
admin.site.register(Requests)
admin.site.register(Admin)
