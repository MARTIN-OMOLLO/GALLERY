from django.test import TestCase

# Create your tests here.
from .models import Picture,Category

# Create your tests here.
def test_instance(self):
        self.assertTrue(isinstance(self.picture, Picture))
        
def tearDown(self):
        self.photos.delete_photos()
        self.category.delete_category()
        self.location.delete_location()
        
def test_save_method(self):
        self.photo.save_photo()
        photos  = Photos.objects.all()
        self.assertTrue(len(Picture)>0)

def test_search_by_category(self):
        photos = Picture.search_picture_by_category('hope')
        self.assertTrue(len(gallery)>0)