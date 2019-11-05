from django.db import models
from django.shortcuts import reverse
from django.conf import settings

# Create your models here.
User = settings.AUTH_USER_MODEL


class BlogPage(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True)
    text = models.TextField()

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.slug)])

    def get_delete_url(self):
        return reverse('delete', args=[str(self.slug)])

    def get_edit_url(self):
        return reverse('edit', args=[str(self.slug)])

    def __str__(self):
        return self.title
