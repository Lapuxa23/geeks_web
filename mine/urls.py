from django.urls import path
from .views import recipe_list, recipe_detail, add_recipe, add_ingredient, delete_recipe

urlpatterns = [
    path('', recipe_list, name='recipe_list'),
    path('recipe/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
    path('recipe/add/', add_recipe, name='add_recipe'),
    path('recipe/<int:recipe_id>/add_ingredient/', add_ingredient, name='add_ingredient'),
    path('recipe/<int:recipe_id>/delete/', delete_recipe, name='delete_recipe'),
]
