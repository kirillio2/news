from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = [category.name for category in Category._meta.fields]
    search_fields = ['name']

    class Meta:
        model = Category
