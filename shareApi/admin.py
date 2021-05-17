from django.contrib import admin
from .models import UserProfile,ShareResult,Share
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered


# Register your models here.
models = apps.get_app_config('shareApi').get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass