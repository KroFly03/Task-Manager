from django.db import models


class Task(models.Model):
    title = models.CharField(verbose_name='Заголовок', unique=True, max_length=100)
    description = models.TextField(verbose_name='Описание')
    completed = models.BooleanField(verbose_name='Выполнена', default=False)
    created_at = models.DateTimeField(verbose_name='Создано', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
