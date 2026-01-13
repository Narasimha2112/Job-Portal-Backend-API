from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    class Roles(models.TextChoices):
        EMPLOYER = "EMPLOYER", "Employer"
        SEEKER = "SEEKER", "Seeker"
        
    username = None
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=120)
    role = models.CharField(
        max_length=20,
        choices=Roles.choices,
        default=Roles.SEEKER
    )
    
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return f"{self.email} ({self.role})"
