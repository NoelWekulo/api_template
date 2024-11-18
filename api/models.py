from django.db import models

# Create your models here.

class Review(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    image=models.ImageField(upload_to='Reviews/')
    message=models.TextField()
    icon = models.CharField(max_length=50) 

    def __str__(self):
        return f"{self.name}"