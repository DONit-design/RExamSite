from django.apps import AppConfig
from django.contrib.auth.apps import AuthConfig


class AccountsConfig(AppConfig):
    name = 'Accounts'
    verbose_name = u'Аккаунты'


class RenameConfig(AuthConfig):
    verbose_name = u'Права и группы'
