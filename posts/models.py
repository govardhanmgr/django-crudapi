from django.db import models

# Create your models here.

"""
class Post:
    id int
    title str(50)
    content text
    created_at datetime
    updated_at datetime
"""

class Post(models.Model):
    title= models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

