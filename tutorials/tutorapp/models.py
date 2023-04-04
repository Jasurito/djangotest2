from django.db import models


class Tutorial(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    published = models.BooleanField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)





