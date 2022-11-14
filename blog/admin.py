from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin

from .models import Post

# Register your models here.



@admin.register(Post)
class PageAdmin(admin.ModelAdmin):
    list_display = ["title",'date_created','date_update','author']
    prepopulated_fields = {"slug": ("title",)}