from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, Group
from django.db import models
# Create your models here.

User = get_user_model()

# class CustomUser(AbstractUser):
#     pass
    # custom_groups = models.ManyToManyField('auth.Group', blank=True, related_name='custom_users')
    # custom_permissions = models.ManyToManyField('auth.Permission', blank=True, related_name='custom_users')


class Category(models.Model):
    names= models.CharField(max_length=255)
    representing_image = models.ImageField(upload_to='category_images', blank=False, null=False)

    class Meta:
        ordering = ('names',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.names


class Item(models.Model):
    category = models.ForeignKey(Category, related_name='item', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='items_images', blank=True, null=True)
    price = models.FloatField()
    stock = models.IntegerField()