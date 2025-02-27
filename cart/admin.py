from django.contrib import admin
from .models import Cart


@admin.register(Cart)
class Product(admin.ModelAdmin):
    pass

