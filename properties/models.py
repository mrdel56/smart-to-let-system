from django.db import models

# Create your models here.

CATEGORY_CHOICES = (
    ("Family", "Family"),
    ("Bachelor", "Bachelor"),
    ("Sublet", "Sublet"),
)


# category management
class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


# location management


class Property(models.Model):
    # category = models.CharField(choices=CATEGORY_CHOICES,max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # space = models.TextField()
    # address = models.TextField()
    # price = models.FloatField(default=0.00)
    # description = models.TextField()
    # property_img = models.ImageField(upload_to='property/', null=True)
    name = models.TextField()
    description = models.TextField()
    # location = models.TextField()
    rooms = models.IntegerField()
    washrooms = models.IntegerField()
    kitchen = models.IntegerField()
    balcony = models.IntegerField()
    floor = models.IntegerField()
    images = models.ImageField(upload_to="property/", null=True)
    visibility = models.BooleanField(default=True)
    price = models.FloatField(default=0.00)

    def __str__(self):
        return f"{self.category} {self.address} {self.price}"
