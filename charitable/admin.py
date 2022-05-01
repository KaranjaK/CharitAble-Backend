from django.contrib import admin

from charitable.models import NGO, Donor, Requests,Admin

# Register your models here.
admin.site.register(NGO)
admin.site.register(Donor)
admin.site.register(Requests)
admin.site.register(Admin)

