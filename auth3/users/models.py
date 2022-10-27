from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import CharField

class User(AbstractUser):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255,unique=True) # unique-уникальное поле
    password = models.CharField(max_length=255)

    USERNAME_FIELD = 'email' # поле имя польз-ля будет заменяться на email-адрес
    REQUIRED_FIELDS = ['username'] # добавили атрибут


