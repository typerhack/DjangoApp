from django.contrib import admin
from .models import Blog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_published','author','article_date')
    list_display_links = ('id','title')
    list_filter = ('author','is_published',)
    list_editable = ('is_published',)
    search_fields = ('title','abstract','article')
    list_per_page = 25

admin.site.register(Blog, BlogAdmin)