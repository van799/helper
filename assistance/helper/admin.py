from django.contrib import admin

# Из модуля models импортируем модель Table
from .models import Table


class TableAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('month', 'data', 'last_name')
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('text',)
    # Добавляем возможность фильтрации по дате
    list_filter = ('data',)


# класс TableAdmin
admin.site.register(Table, TableAdmin)
