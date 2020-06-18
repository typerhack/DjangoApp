from django.contrib import admin
from .models import Contact


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'email', 'phone', 'contact_date_report')
    list_display_links = ('id', 'subject')
    search_fields = ('subject', 'email', 'message')
    list_per_page = 25


admin.site.register(Contact, ContactAdmin)
