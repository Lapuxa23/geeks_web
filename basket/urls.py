from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.books_list, name='book_list_html'),
    path('add-to-cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
]
