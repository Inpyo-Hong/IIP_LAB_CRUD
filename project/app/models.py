from django.db import models
from uuid import uuid4
from datetime import datetime
import os

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    writer = models.CharField(max_length=100, default='')
    file = models.FileField('첨부파일', null=True, blank=True,  upload_to='')

    def __str__(self):
        return self.title

