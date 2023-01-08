from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your views here.



class User(AbstractUser):
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True)

    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []