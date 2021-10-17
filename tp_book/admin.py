from django.contrib import admin
from tp_book.models import Book


class AdminMode(admin.ModelAdmin):
    list_display = ['Author', 'store_name', 'fav']
    search_fields = ['Author', 'store_name']


admin.site.register(Book, AdminMode)
