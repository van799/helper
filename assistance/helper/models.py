from django.db import models


class Table(models.Model):
    """Создаем модель таблицы дежурст,
    которая включает в себя (месяц, фамилия, дата)."""
    month = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    data = models.CharField(max_length=50)

