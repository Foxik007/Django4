from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=200,db_index=True)
    content = models.TextField(max_length=5000,blank=True, null=True, help_text='Введите описание')
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images',)
    slug = models.SlugField(max_length=50,unique=True)
    likes = models.ManyToManyField(User,related_name='PostComment',blank=True)
    reply = models.ForeignKey('self',null=True,related_name='reply_ok',on_delete=models.CASCADE)
    tags = TaggableManager()
    class Meta:
        verbose_name = 'Создать пост'
        verbose_name_plural = 'Создать посты'
    def total_likes(self):
        return self.likes.count()
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
