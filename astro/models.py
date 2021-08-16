from django.db import models

# Create your models here.
class Astro_details(models.Model):
    
    name = models.CharField(max_length=60)
    img = models.ImageField(upload_to='profile_img')
    speciality = models.CharField(max_length=200)
    exp = models.IntegerField()
    language = models.CharField(max_length=60)
   