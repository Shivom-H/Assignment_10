from django.db import models
from django.utils import timezone

# Create your models here.

class course(models.Model):
    course_id = models.AutoField
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)
    price = models.IntegerField()
    image = models.ImageField(upload_to="course\images",default="https://via.placeholder.com/500x500.png?text=Default")
    pub_date = models.DateField(default=timezone.now)
    category = models.CharField(max_length=50, default="web")
    def __str__(self):
        return self.name

class contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50,default="")
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)
    phone = models.IntegerField()
    screenshot = models.ImageField(upload_to="contact\images",default="https://via.placeholder.com/500x500.png?text=Default")
    pub_date = models.DateField(default=timezone.now)
    def __str__(self):
        return self.name

class order(models.Model):
    jsonCart = models.CharField(max_length=250)
    email = models.CharField(max_length=50,default="")
    state = models.CharField(max_length=50)
    isSameBillingAddress = models.BooleanField(default="False")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    zip = models.IntegerField()
    order_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.email