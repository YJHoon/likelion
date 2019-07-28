from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=True)
    view_count = models.IntegerField(default=0)
    time = models.IntegerField(default=0)
    image = models.ImageField(upload_to="images/", null=True)
    category = models.CharField(max_length=200)
    ingredient = models.CharField(max_length=200)
    level = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title