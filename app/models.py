
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    email = models.EmailField()
    username = models.CharField(max_length = 200)
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200)
    description = models.CharField(max_length=200)
    city = models.CharField(max_length = 200)
    zip = models.IntegerField(null = True)
    state = models.CharField(max_length = 200)
    img = models.ImageField(upload_to = 'display_picture',blank = True)

class Advertisement(models.Model):
    category_CHOICES =( 
    ("Buy", "Buy"), 
    ("Sell", "Sell"), 
) 
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'ads',blank = False)
    item_name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 200)
    quantity = models.IntegerField()
    cost = models.IntegerField()
    status = models.CharField(max_length = 20,default = "Not Sold")
    category = models.CharField(max_length = 4,choices = category_CHOICES)



