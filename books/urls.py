from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list_view, name='book_list'),
    path('film_detail/<int:id>/', views.book_detail_view, name='book_detail'),

    path("about_me/", views.about_me, name='about_me'),
    path("text_photo/", views.text_photo, name='text_photo'),
    path("time_now/", views.time_now, name='time_now'),
]