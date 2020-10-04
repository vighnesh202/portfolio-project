# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 12:32:36 2020

@author: vighnesh.paramasivam
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('<int:blog_id>/', views.detail, name='detail')]