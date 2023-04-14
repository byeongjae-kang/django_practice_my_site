from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MinLengthValidator


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def full_name(self):
        return f"{self.first_name}, {self.last_name}"

    def __str__(self) -> str:
        return self.full_name()


class Tag(models.Model):
    caption = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(
        Author, null=True, related_name="post", on_delete=models.SET_NULL
    )
    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return f"{self.title}, {self.slug}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("post", args=[self.slug])
