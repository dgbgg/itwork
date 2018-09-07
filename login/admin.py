from django.contrib import admin
from login.models import *  # 导入所有模型类

# Register your models here.



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'password', 'outlet', 'email', 'identity', 'c_time', 'has_confirmed')  
    list_filter = ('identity', 'c_time', 'outlet',) #过滤器
    #search_fields =('name', 'email') #搜索字段
    #date_hierarchy = 'c_time'    # 详细时间分层筛选　
    list_editable = ['identity']
    fk_fields = ('email',)


@admin.register(ConfirmString)
class ConfirmStringAdmin(admin.ModelAdmin):
    list_display = ('code', 'user', 'c_time')  




admin.site.site_header = '后台管理'
admin.site.site_title = '科技与产品管理部 工作平台'