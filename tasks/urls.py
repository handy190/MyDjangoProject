#! /usr/bin/python
# encoding=utf-8

"""
@Author  :  Steven
@Date    :  2021/9/1 03:39
@Desc    :  function description
"""
from rest_framework import routers
from django.urls import path, re_path
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


# router = DefaultRouter()
# router.register(r'tasks', viewset=views.TaskViewSet)

task_list = views.TaskViewSet.as_view(
    {
        'get': 'list',
        'post': 'create'
    }
)

task_detail = views.TaskViewSet.as_view(
    {
        'get': 'retrieve',  # 只处理get请求，获取单个记录
    }
)

urlpatterns = [
    path(r'dashboard/', views.dashboard, name='dashboard'),
    re_path(r'^users/$', views.UserList.as_view()),
    re_path(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    re_path(r'^tasks/$', task_list),
    re_path(r'^tasks/(?P<pk>[0-9]+)/$', task_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
# urlpatterns += router.urls