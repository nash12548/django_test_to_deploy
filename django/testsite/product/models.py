from django.db import models
from django.core.files.storage import FileSystemStorage
from django.urls import reverse


# class ProductQuerySet(models.QuerySet):
#     def image(self):
#         return self.filter(title='Aram')


# Create your models here.
class ProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset.all().filter(title='Aram')


class Product(models.Model):
    title = models.CharField(max_length=32)
    product_description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='product/')

    # objects = models.Manager()
    # aram_objects = ProductManager()
    def get_absolute_url(self):
        # return '{pk}'.format(pk=self.id)
        return reverse('product_detail_page', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
