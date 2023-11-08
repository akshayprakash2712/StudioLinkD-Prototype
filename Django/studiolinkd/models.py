from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

# Create your models here.
class UserType(AbstractUser):    
    CHOICES = [
        ("A", "Artist"),
        ("B", "Client"),
        ("C", "Tv"),
        ("D","Radio")
    ]

    TYPE_CHOICES = models.CharField(
        max_length=1,
        choices=CHOICES,
        default="A",
        )
    def clean(self):
        if (
            self.TYPE_CHOICES
            and sum(
                [
                    self.TYPE_CHOICES == "A",
                    self.TYPE_CHOICES == "B",
                    self.TYPE_CHOICES == "C",
                    self.TYPE_CHOICES == "D",
                ]
            )   
            != 1
        ):
            raise ValidationError("Only one option can be selected.")
    
class UserRegistrationModel(models.Model):
    pass

class Artist(models.Model):
    name=models.CharField(max_length=120)
    type=models.CharField(max_length=120)
    location = models.CharField(max_length=100)
    image = models.ImageField(default='pic.jpg',upload_to="") 
    active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Client(models.Model):
    name=models.CharField(max_length=120)
    description=models.TextField(blank=True,null=True)
    image = models.ImageField(default='pic.jpg',upload_to="") 
    active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name        

class TvChannel(models.Model):
    name=models.CharField(max_length=120)
    description=models.TextField(blank=True,null=True)
    image = models.ImageField(default='pic.jpg',upload_to="") 
    active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name                

class RadioChannel(models.Model):
    name=models.CharField(max_length=120)
    description=models.TextField(blank=True,null=True)
    image = models.ImageField(default='pic.jpg',upload_to="") 
    active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name               
    