from django.db import models
from authentications.models import User

from helpers.models import TrackingModel
from authentications.models import User

# Create your models here.

class Todo(TrackingModel):
    title=models.CharField(max_length=255)
    description=models.TextField()
    is_complete=models.BooleanField(default=False)
    owner=models.ForeignKey(to=User,on_delete=models.CASCADE)


    class Meta:
        ordering=['title']


    def __str__(self):
        return self.title