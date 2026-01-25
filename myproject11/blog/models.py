from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField(unique=True)
    enrollment_date=models.DateField(auto_now_add=True)
    city =models.CharField(max_length=100,default='Unknown')
    def __str__(self):
        return self.name    
class Profile(models.Model):
    user=models.CharField(max_length=100)
    bio=models.TextField()
    location=models.CharField(max_length=100)
    
    def __str__(self):
        return self.user    