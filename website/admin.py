from django.contrib import admin
from .models import Popular_Destination, Image, Package, Pack_Desc, Cab, Inclusions
# Register your models here.

admin.site.register(Popular_Destination)
admin.site.register(Image)
admin.site.register(Package)
admin.site.register(Pack_Desc)
admin.site.register(Cab)
admin.site.register(Inclusions)