from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=10)  # Исправлено
    description = models.CharField(max_length=100)  # Исправлено
    ADD = 'Добавлено'
    WORK = 'В работе'
    READY = 'Выполнено'
    STATUS = [
        (ADD, 'Добавлено'),
        (WORK, 'В работе'),
        (READY, 'Выполнено'),
    ]

    level = models.CharField(max_length=10, choices=STATUS, default=ADD)  # Добавлено поле уровня

    def __str__(self):
        return self.name