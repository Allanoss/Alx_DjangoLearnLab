# LibraryProject/bookshelf/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import BookSearchForm, CustomUserRegistrationForm
from .models import Book

class ExampleForm(forms.Form):
    example_field = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Example Field'}),
    )
    
def search_books(request):
    if request.method == 'POST':
        form = BookSearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            books = Book.objects.filter(title__icontains=query)
            return render(request, 'bookshelf/book_list.html', {'books': books})
    else:
        form = BookSearchForm()

    return render(request, 'bookshelf/search_books.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserRegistrationForm()

    return render(request, 'bookshelf/register.html', {'form': form})
