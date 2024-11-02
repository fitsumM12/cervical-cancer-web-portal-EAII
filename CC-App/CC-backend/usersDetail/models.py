from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

class HealthyInstitution(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class usersDetail(AbstractUser):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('BLOCKED', 'Blocked')
    ]
    ROLE_CHOICES = [
        ('SUPER ADMIN', 'Super Admin'),
        ('ADMIN', 'Admin'),
        ('USER', 'User') 
    ]
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=110, blank=True, null=True, choices=GENDER_CHOICES)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    zone = models.CharField(max_length=100, blank=True, null=True)
    kebele = models.CharField(max_length=100, blank=True, null=True)
    hospital = models.CharField(max_length=100, blank=True, null=True)
    health_institution = models.ForeignKey(HealthyInstitution, on_delete=models.CASCADE)
    image = models.CharField(max_length=100, blank=True, null=True)
    passport = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=12, blank=True, null=True, choices=STATUS_CHOICES)
    role = models.CharField(max_length=110, blank=True, null=True, choices=ROLE_CHOICES)
    def __str__(self):
        return self.username

