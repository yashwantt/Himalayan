from .views import *
from django.urls import path

urlpatterns = [
    path('', home, name = 'home'),
    path('cabs/', cabs, name = 'cabs'),
    path('package/<str:pack>/', pack, name = 'package'),
    path('destination/<str:city>/', destination, name = 'destination'),
    path('mail/', mail, name = 'mail'),
]
