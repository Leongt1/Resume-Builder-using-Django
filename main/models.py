from django.db import models

# Create your models here.
class Profile(models.Model):
    # personal infomation
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=20)    
    address = models.CharField(max_length=1000)
    insta = models.CharField(max_length=100)
    github = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    # professional information
    careerObj = models.TextField(max_length=500)
    workexp = models.TextField(max_length=1000)
    project = models.TextField(max_length=1000)
    skill = models.CharField(max_length=100)
    aq = models.TextField(max_length=1000)

    def __str__(self):
        return self.name