from django.db import models
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.

class SiteContent(models.Model):
    slug = models.SlugField(unique=True)  # örn: 'hakkimda', 'anasayfa-alt-metin'
    baslik = models.CharField(max_length=200, blank=True)
    icerik = models.TextField(blank=True)
    guncellenme_tarihi = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slug
    
class category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'

class yazi(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    imageUrl = models.ImageField(upload_to='uploads', blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    isActive = models.BooleanField(default=True)
    slug = models.SlugField(default="", null=False,unique=True,db_index=True)
    tarih = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(category,default=1, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(args,kwargs)

    def __str__(self):
        return f'{self.title} {self.date}'
