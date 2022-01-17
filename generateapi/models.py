from django.db import models
import uuid
import datetime
import pytz




class MyUUIDModel(models.Model):
   
   id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
   created_at=models.DateTimeField(auto_now_add=True, null=True)
   

   class Meta:
       ordering=['-created_at'] 
    
#    def __str__(self):
#         return f"self.id"