from django.contrib.auth.models import User
from django.db import models

# Create your models here.


# manage user roles
class Role(models.Model):
    role_name = models.CharField(max_length=100)

    def __str__(self):
        return self.role_name


# manage user information
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11 , null=True)
    address = models.TextField( null=True)
    image = models.ImageField(upload_to="user/", null=True)
    credit = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
