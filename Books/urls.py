from django.urls import path
from .views import BooksFromStorage

app_name = 'books'

urlpatterns = [
    
    path('', BooksFromStorage.as_view(), name ='books_list')
    
]
