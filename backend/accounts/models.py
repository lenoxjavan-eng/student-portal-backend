from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_STUDENT = 'student'
    ROLE_ADMIN = 'admin'
    ROLE_CHOICES = [(ROLE_STUDENT, 'Student'), (ROLE_ADMIN, 'Admin')]

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=ROLE_STUDENT)
    phone = models.CharField(max_length=20, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
