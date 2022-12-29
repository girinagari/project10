from django.urls import path
from app1.views import *

urlpatterns=[
    path('hai/',hai,name='hai'),
    path('hello/',hello,name='hello'),
]