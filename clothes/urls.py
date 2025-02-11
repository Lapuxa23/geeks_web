from django.urls import path
from . import views
from .views import all_clothes

urlpatterns = [
    path('all_clothes/',views.all_clothes,name='all_clothes'),
    path('children_clothes/',views.all_clothes,name='children_clothes'),
    path('teenager/',views.all_clothes,name='teenager_clothes'),
    path('adult/',views.all_clothes,name='adult_clothes'),
]