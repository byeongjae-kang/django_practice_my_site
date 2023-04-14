from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.first_name}, {self.last_name}"


class Tag(models.Model):
    caption = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(blank=True)
    content = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return f"{self.title}, {self.slug}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("post", args=[self.slug])
