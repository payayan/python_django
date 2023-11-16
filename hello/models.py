from django.db import models

# Create your models here.
class Article(models.Model):

    content = models.CharField(max_length = 140)

    def __str__(self):
        return self.content