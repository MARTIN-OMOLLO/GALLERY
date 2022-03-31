from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
# class Location(models.Model):
#     name = models.CharField(max_length =30)
#     def __str__(self):
#         return self.name

#     def save_location(self):
#         self.save()

#     def delete_location(self):
#         self.delete()

class category(models.Model):
    name = models.CharField(max_length =30)
    def __str__(self):
        return self.name

    @classmethod
    def search_by_category(cls, search_term):
        category = cls.objects.filter(name__icontains=search_term)
        return category
    

class Photos(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
    category = models.ForeignKey(category , on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image')
    # location = models.ManyToManyField(Location)
    def __str__(self):
        return self.title
    def save_photo(self):
        self.save()

    def delete_photo(self):
        self.delete()


