from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    url = models.URLField(null=True)
    def __str__(self):
        return self.title