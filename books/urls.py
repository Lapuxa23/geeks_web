from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list_view, name='book_list'),
#    path('<int:pk>/', views.book_detail_view, name='book_detail_view'),
    path('photo/', views.text_photo, name='text_photo'),
    path('about/', views.about_me, name='about_me'),
]

