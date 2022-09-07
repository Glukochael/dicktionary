from django.db import models


class Word(models.Model):
    name = models.CharField('Слово', max_length=200)
    definition = models.TextField('Определение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Слово'
        verbose_name_plural = 'Слова'