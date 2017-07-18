#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: urls.py
@time: 2017/7/18 17:00
"""

from django.conf.urls import url
from apps import views

urlpatterns = [
    url(r'^fenye/$', views.page),
]