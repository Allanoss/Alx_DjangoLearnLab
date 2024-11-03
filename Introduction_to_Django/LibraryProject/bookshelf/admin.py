from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    # Display title, author, and publication year in list view
    list_display = ('title', 'author', 'publication_year')
    # Enable search functionality for title and author fields
    search_fields = ('title', 'author')
    # Add filter options for publication year
    list_filter = ('publication_year',)

# Register the Book model with the custom admin configurations
admin.site.register(Book, BookAdmin)