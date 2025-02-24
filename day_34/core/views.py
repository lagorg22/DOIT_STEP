from .models import Author, Book, Category
from django.shortcuts import render, redirect
from .forms import BookForm

def index(request):

    return render(request, 'index.html')

def list_books(request):

    books = Book.objects.all()

    return render(request, 'list_books.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('list_books')
    else:
        form = BookForm()

    return render(request, 'add_book.html', {'form': form})
