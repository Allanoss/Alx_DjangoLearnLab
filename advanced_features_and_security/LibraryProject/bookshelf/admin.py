from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

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

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'username', 'date_of_birth', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('username', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'date_of_birth', 'profile_photo', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'username')
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)