#! /usr/bin/python
# encoding=utf-8

"""
@Author  :  Steven
@Date    :  2021/9/1 02:08
@Desc    :  function description
"""
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from tasks.models import Task


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('id', 'author', 'create_date')


class GroupSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name', 'age', 'sex']


class TaskSerializer(ModelSerializer):
    # author = serializers.ReadOnlyField(source="author.username")
    cn_status = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = '__all__'
        # fields = ['name', 'status', 'age', 'sex']

    def get_cn_status(self, obj):
        if obj.status == 'f':
            return "已发表"
        elif obj.status == 'u':
            return "草稿"
        else:
            return ''
