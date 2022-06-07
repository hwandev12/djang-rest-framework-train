from sre_constants import CATEGORY
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    pass


CATEGORY_CHOICES = (
    ('Dj', 'Django'),
    ('Py', 'Python')
)

# create class model here
class Posts(models.Model):
    title = models.CharField(max_length=100)
    post_id = models.IntegerField()
    category = models.TextField(max_length=255, choices=CATEGORY_CHOICES)
    start_date = models.DateTimeField(auto_now_add=True)
    change_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
