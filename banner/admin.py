from django.contrib import admin
from .models import Banner


# Register your models here.
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'banner_persian_date_report', 'is_published')
    list_display_links = ('id', 'project_name')
    list_filter = ('is_published',)
    list_editable = ('is_published',)
    search_fields = ('project_name',)
    list_per_page = 25


admin.site.register(Banner, BannerAdmin)
