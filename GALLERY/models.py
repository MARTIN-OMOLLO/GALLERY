from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Category(models.Model):
    first_name = models.CharField(max_length =30)
    

class Photos(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image')
