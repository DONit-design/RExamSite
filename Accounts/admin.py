from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from Accounts.forms import UserCreateForm
from .models import RExamUserModel, StudyGroupModel


class RExamUserAdmin(UserAdmin):
    form = UserCreateForm
    fieldsets = (
        (u'Основная информация', {'fields': ('username', 'email', 'password')}),
        (u'Личные данные', {'fields': ('last_name', 'first_name', 'middle_name', 'study_group')}),
        (u'Разрешения', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions'),
        }),
        (u'Второстепенные данные', {'fields': ('last_login', 'date_joined')}),
    )


# Register your models here.
admin.site.register(StudyGroupModel)
admin.site.register(RExamUserModel, RExamUserAdmin)
