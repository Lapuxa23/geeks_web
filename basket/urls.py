from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('add-to-cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
]
