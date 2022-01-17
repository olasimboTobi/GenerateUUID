from django.urls import path 
from generateapi import views


# from django.urls import path
# from generateapi.views import MyUUIDModelAPIView

urlpatterns = [
    path('', views.MyUUIDModel_list,
    name='MyUUIDModel_list')
]

