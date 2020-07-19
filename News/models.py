from django.db import models
from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField(name='title', max_length=50)
    body = models.TextField(name='body')
    pub_date = models.DateTimeField(name='pub_date')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Messages(models.Model):
    name = models.CharField(name='name', max_length=50)
    email = models.EmailField(name='email')
    subject = models.CharField(name='subject', max_length=50)
    message = models.TextField(name='message')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Commentary(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    commentary_text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(name='Date', auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
