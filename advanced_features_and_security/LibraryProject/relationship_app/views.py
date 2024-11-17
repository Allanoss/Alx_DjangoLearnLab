from django.shortcuts import render, get_object_or_404
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.http import HttpResponseBadRequest

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

def search_books(request):
    query = request.GET.get('q', '')
    if not query.isalpha():  # Validate input to prevent dangerous characters
        return HttpResponseBadRequest("Invalid search query.")
    
    books = Book.objects.filter(title__icontains=query)
    return render(request, 'bookshelf/book_list.html', {'books': books})    