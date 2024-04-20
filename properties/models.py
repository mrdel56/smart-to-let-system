from django.db import models

# Create your models here.

CATEGORY_CHOICES = (
    ('Family','Family'),
    ('Bachelor','Bachelor'),
    ('Sublet','Sublet'),
)
class Property(models.Model):
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=100)
    space = models.TextField()
    address = models.TextField()
    price = models.FloatField(default=0.00)
    description = models.TextField()
    property_img = models.ImageField(upload_to='property/', null=True)


    def __str__(self):
        return f"{self.category} {self.address} {self.price}"