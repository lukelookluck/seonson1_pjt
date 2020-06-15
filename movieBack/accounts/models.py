from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, Model
from django_mysql.models import ListCharField

# Create your models here.

class User(AbstractUser):
  pass
  # like_movie = ListCharField(
  #   base_field=CharField(max_length=10),
  #       size=6,
  #       max_length=(6 * 11)
  # )
  