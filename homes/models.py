'''
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Credentials(models.Model):
    email_address = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)
    name = models.CharField(max_length = 30)
    #image = models.ImageField(default = "img.txt", blank = True)
    creation_date = models.DateTimeField(auto_now_add= True)


    class Meta:
        verbose_name_plural = "credentials"

    def __str__(self):
        return self.name

'''