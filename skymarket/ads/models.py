from django.conf import settings
from django.db import models

from users.models import User


class Ad(models.Model):
    title = models.CharField(max_length=200)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField(max_length=1000, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, upload_to='logos/')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Comment(models.Model):
    # TODO добавьте поля модели здесь
    text = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']

    def __str__(self):
        return self.text
