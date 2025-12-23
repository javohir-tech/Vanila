from django.db import models
from django.contrib.auth.models import AbstractUser, User

# from django.contrib.auth
#
# class User(AbstractUser):
#     photo = models.ImageField(upload_to='user/' , blank=True)
#     address = models.CharField(max_length=150)
#     date_of_birth = models.DateTimeField()


class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , related_name='profile')
    image = models.ImageField(upload_to="users/", blank=True, null=True)
    date_of_birth = models.DateTimeField(blank=True , null=True)
    
    def __str__(self):
        return f"{self.user.username} ni profili"


# Create your models here.
