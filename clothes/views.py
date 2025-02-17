from django.views.generic import ListView
from django.shortcuts import render
from .models import Product


class AllClothesView(ListView):
    model = Product
    template_name = 'clothes_a/all_clothes.html'
    context_object_name = 'all_clothes'
    ordering = ['-id']


class ChildrenClothesView(ListView):
    model = Product
    template_name = 'clothes_a/children_clothes.html'
    context_object_name = 'children_clothes'

    def get_queryset(self):
        return Product.objects.filter(tags__name='для детей').order_by('-id')


class TeenagerClothesView(ListView):
    model = Product
    template_name = 'clothes_a/teenager_clothes.html'
    context_object_name = 'teenager_clothes'

    def get_queryset(self):
        return Product.objects.filter(tags__name='для подростков').order_by('-id')


class AdultClothesView(ListView):
    model = Product
    template_name = 'clothes_a/adult_clothes.html'
    context_object_name = 'adult_clothes'

    def get_queryset(self):
        return Product.objects.filter(tags__name='для взрослых').order_by('-id')
