from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.TextField()
    pic=models.ImageField()

class Topic(models.Model):
    topic=models.CharField(max_length=100,primary_key=True)
    
    def __str__(self) -> str:
        return self.topic

class Webpage(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()

    def __str__(self) -> str:
        return self.name

class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField()
    author=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.author