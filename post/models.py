from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from main import settings


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    text = models.CharField(max_length=150)
    slug = models.SlugField(max_length=50)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes1')
    dislikes = models.IntegerField(default=0)
    created_date = models.DateTimeField(
        auto_now_add=True)

    @property
    def total_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.author)
        super(Post, self).save(*args, **kwargs)

    # published_date = models.DateTimeField(
    #     blank=True, null=True)
    # image = models.ImageField(null=True, blank=True, upload_to="image/",
    #                           verbose_name="image")
    # category = TreeForeignKey(Category, blank=True, null=True, related_name='cat')
    # keywords = models.ManyToManyField(Keywords, related_name="keywords", related_query_name="keyword", verbose_name='Теги')

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    # def __str__(self):
    #     return self.title

class Follows(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    follows = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followed_by')

    def __str__(self):
        return self.user.username