from django.urls import path
from . import views

urlpatterns = [
    path('anilibria_schedule/', views.AnilibriaScheduleView.as_view(), name='anilibria_schedule'),
    path('anilibria_parsing/', views.AnilibriaFormView.as_view(), name='anilibria_parser'),
]
