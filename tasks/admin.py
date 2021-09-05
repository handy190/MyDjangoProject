from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Task

admin.site.site_header = 'Django管理后台'  # 设置header
admin.site.site_title = 'Django管理后台'  # 设置title
admin.site.index_title = 'Django管理后台'

admin.site.register(Task)
