from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list_view, name='book_list'),
    path('book/<int:id>/', views.book_detail_views, name='book_detail'),
    path('time/', views.time_now, name='time_now'),
    path('photo/', views.text_photo, name='text_photo'),
    path('about/', views.about_me, name='about_me'),
]

