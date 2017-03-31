from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator

class Usr(AbstractUser):
    username = models.EmailField(('Adres e-mail'), unique=True, validators=[EmailValidator])
    USERNAME_FIELD = 'username'

