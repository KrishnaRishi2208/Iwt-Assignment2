from django.db import models

# Create your models here.
from pickle import TRUE
from django.db import models
class users(models.Model):
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    Email= models.EmailField(max_length=60, blank=TRUE)
    City= models.CharField(max_length=30, blank=TRUE)
    PreviousProcedures= models.CharField(max_length=300, blank=TRUE)