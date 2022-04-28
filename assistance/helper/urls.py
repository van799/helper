from django.urls import path

from . import views

app_name = 'helper'

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    # Страница создания расписания
    path('create_helper/', views.create_helper, name='create_helper'),

]
