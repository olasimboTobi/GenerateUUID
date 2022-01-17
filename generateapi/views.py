
from django.shortcuts import render
from rest_framework import status
from generateapi.models import MyUUIDModel
from generateapi.serializers import MyUUIDModelSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions, status
import datetime





@api_view(['GET'])
def MyUUIDModel_list(request):
    
    serializers_class = MyUUIDModelSerializer
    permission_classes = [permissions.AllowAny]
    if request.method == 'GET':
        data = dict()
        MyUUIDModel.objects.create()
        queryset = MyUUIDModel.objects.all()
        serializers_class= MyUUIDModelSerializer(queryset, many=True)

        for instance in serializers_class.data:
           data[instance['created_at']] = instance['id']

           
        return Response(data, status=status.HTTP_200_OK)
       
    
