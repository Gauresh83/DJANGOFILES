from django.db import models

class Student(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.TextField()
    photo = models.ImageField(upload_to="students/", null=True, blank=True)

    def __str__(self):
        return self.name