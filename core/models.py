from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

class SiteSetting(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='site/')
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    about = models.TextField()
    mission = models.TextField()
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Advantage(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text="Имя иконки из Font Awesome")

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='news/')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

User = get_user_model()
class ContactMessage(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новый'),
        ('processed', 'Обработан'),
        ('published', 'Опубликован с ответом'),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Телефон", blank=True)
    message = models.TextField(verbose_name="Сообщение")
    answer = models.TextField(verbose_name="Ответ", blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%d.%m.%Y')}"

    def is_published(self):
        return self.status == 'published'