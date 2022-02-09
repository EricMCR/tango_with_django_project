# -*- coding = utf-8 -*-
# @TIME : 2022/1/27 23:20
# @Author : Eric Ma
# @File : urls.py
# @Software : PyCharm

from django.urls import path
from rango import views

app_name = 'rango'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about')
]