from django.db import models
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField()
    originalprice=models.IntegerField()
    discountedprice=models.IntegerField()
    image=models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, null=True)

    def get_absolute_url(self):
        return reverse("welcome",kwargs={"slug":self.slug})


class Checkout(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    emailId = models.CharField(max_length=50)
    phoneNo = models.IntegerField()
    price = models.IntegerField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=40)
    pincode = models.IntegerField()
    address = models.TextField()

