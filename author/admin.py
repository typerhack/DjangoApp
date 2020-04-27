from django.contrib import admin
from .models import Author

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','email','phone','start_date')
    list_display_links = ('id','first_name','last_name')
    search_fields = ('first_name','last_name',)
    list_per_page = 25

admin.site.register(Author,AuthorAdmin)