from django.db import models

# Create your models here.

class Board(models.Model):
    language = models.IntegerField()
    subject = models.CharField(max_length=10)
    memo = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.subject