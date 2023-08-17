from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model

from urllib.parse import quote

User = get_user_model()


# Create your models here.

STATUS_CHOICES = (
    ('pending', 'pending'),
    ('public', 'public'),
)
RAITING_CHOICE = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10'),
)

class MangaList(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    cover = models.ImageField(upload_to='manga/cover/')
    manga_type = models.ManyToManyField('Type')
    episodes = models.IntegerField(default=0)
    category = models.ManyToManyField('Category')
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    slug = models.SlugField(unique=True, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.id:
            super().save(*args, **kwargs)
        
        if not self.slug:
            self.slug = quote(f'{self.id}/{self.title}')
        super().save(*args, **kwargs)
    
    @property
    def average_raiting(self):
        total_raitings = Raiting.objects.filter(manga=self).aggregate(models.Avg('value'))
        avg_rating = total_raitings['value__avg']
        if avg_rating is not None:
            return round(avg_rating, 2)
        return 0
    
class Raiting(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='manga_ratings')
    manga = models.ForeignKey(MangaList, related_name='ratings', on_delete=models.SET_NULL, null=True)
    value = models.PositiveIntegerField(choices=RAITING_CHOICE)
    
    def __str__(self):
        return f'{self.user.username} - {self.value}'
    
    class Meta:
        unique_together = ['manga', 'user'] 

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    