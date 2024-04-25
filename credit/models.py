from django.db import models

# from properties.models import PropertyOwner
from properties.models import User

# Create your models here.


# credit package management
class CreditPackage(models.Model):
    package_name = models.CharField(max_length=100)
    price = models.FloatField(default=0.00)
    credit = models.IntegerField()

    def __str__(self):
        return self.package_name


# transaction management


class Transaction(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    package = models.ForeignKey(CreditPackage, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100)
    amount = models.FloatField(default=0.00)
    date = models.DateTimeField(auto_now_add=True)
    transaction_method = models.CharField(max_length=100)

    def __str__(self):
        return self.transaction_id
