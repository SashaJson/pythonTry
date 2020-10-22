from django.db import models


class Articles(models.Model):
    title = models.CharField('title', max_length=50)
    anons = models.CharField('anons', max_length=50)
    full_text = models.TextField('body article')
    date = models.DateTimeField('Date push article')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'piece of news'
        verbose_name_plural = 'news'
