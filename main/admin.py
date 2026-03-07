from django.contrib import admin

from main.models import contact as models
from main.models import category as ctg
# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    search_fields=("f_name",)
    list_display_links =("id", "f_name")
    list_display=("id", "f_name", "phone","email","image","category","address","notes","created_at","updated_at")

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=("id","name")
