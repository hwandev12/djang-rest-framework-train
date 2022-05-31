from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    pass


# create class model here
class Posts(models.Model):
    title = models.CharField(max_length=100)

    def __str_(self):
        return self.title
