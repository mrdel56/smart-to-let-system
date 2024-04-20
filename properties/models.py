from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# CATEGORY_CHOICES = (
#     ("Family", "Family"),
#     ("Bachelor", "Bachelor"),
#     ("Sublet", "Sublet"),
# )


# property owner management
class PropertyOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nid = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    properties = models.ManyToManyField("Property", related_name="property_owner")

    def __str__(self):
        return self.user.username


# category management
class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


# location management
class Location(models.Model):
    road_no = models.CharField(max_length=100)
    post_code = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    division = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.road_no} {self.post_code} {self.district} {self.division} {self.country}"


class Property(models.Model):
    # category = models.CharField(choices=CATEGORY_CHOICES,max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    # space = models.TextField()
    # address = models.TextField()
    # price = models.FloatField(default=0.00)
    # description = models.TextField()
    # property_img = models.ImageField(upload_to='property/', null=True)
    name = models.TextField()
    description = models.TextField()
    rooms = models.IntegerField()
    washrooms = models.IntegerField()
    kitchen = models.IntegerField()
    balcony = models.IntegerField()
    floor = models.IntegerField()
    property_img = models.ImageField(upload_to="property/", null=True)
    visibility = models.BooleanField(default=True)
    price = models.FloatField(default=0.00)

    def __str__(self):
        return self.name


# property review management
class Review(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.review


# booking management
class Booking(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    booking_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.property} {self.user} {self.booking_date} "
