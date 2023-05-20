from django.db import models

# Create your models here.
class Works(models.Model):
    caption = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    video =models.FileField(upload_to='video/%y',blank=True) 

    def __str__(self):
        return self.caption
    
    def snippet(self):
        return self.body[:49] + ' ...'
    