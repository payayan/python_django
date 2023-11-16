from django.db import models

# Create your models here.
from django.contrib.auth.models import User 
from django.urls import reverse

class Article(models.Model):
    content = models.TextField(max_length = 140)
    author = models.ForeignKey(User, on_delete = models.PROTECT)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


    def __str__(self):
        return self.content


    def get_absolute_url(self):
        return reverse('bbs:detail', kwargs = {'pk': self.pk})  