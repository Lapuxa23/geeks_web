from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from users.views import my_recipes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),
    path('', include('clothes.urls')),
    path('', include('basket.urls')),
    path('', include('anilibria_schedule.urls')),
    path('', include('users.urls')),
    path('mine/', my_recipes, name='my_recipes'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)