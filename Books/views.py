from django.shortcuts import render
from django.views.generic import ListView
from .models import BookList
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class BooksFromStorage(LoginRequiredMixin,ListView):
    model = BookList
    template_name = 'Books/books.html'
    context_object_name ='allbook'
    ordering = ['-book_name']
    paginate_by = 6

    #def display_list(request):
    #return render(request, 'Books/books.html')