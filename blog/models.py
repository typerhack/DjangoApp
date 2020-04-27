from django.db import models
from datetime import  datetime
from author.models import Author

# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    abstract = models.CharField(max_length=400)
    article = models.TextField()
    video_link = models.URLField(blank=True)
    photo_main = models.ImageField(upload_to='photos_article/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos_article/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos_article/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos_article/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos_article/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos_article/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=False)
    article_date = models.DateTimeField(default=datetime.now())
    def __str__(self):
        return self.title