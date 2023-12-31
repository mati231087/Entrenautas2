from django.db import models
from usuario.models import CustomUser

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=10000)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    def __str__(self):
        return self.title
class Comment(models.Model):
    content = models.TextField(max_length=10000)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    def __str__(self):
        return self.content
    
