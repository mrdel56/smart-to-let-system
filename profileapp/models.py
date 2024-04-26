from django.contrib.auth.models import User
from django.db import models

# Create your models here.


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # Add other fields as needed


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile", null=True
    )
    name = models.CharField(default="Mr. Jhon", max_length=200, null=True)
    user_rule = models.CharField(
        max_length=100, default="Tenant or Landlord or Admin", null=True
    )
    profession = models.CharField(max_length=100, null=True)
    profile_img = models.ImageField(upload_to="profile", null=True, blank=True)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.user.username
