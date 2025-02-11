from django.shortcuts import render
from . import models


def all_clothes(request):
    if request.method == "GET":
        query = models.Product.objects.all().order_by('-id')
        context_object_name = {
            'all_clothes': query
        }
        return render(request, 'clothes_a/all_clothes.html',
                      context=context_object_name)


def children_clothes(request):
    if request.method == "GET":
        query = models.Product.objects.filter(tags__name='для детей').order_by('-id')
        context_object_name = {
            'children_clothes': query
        }
        return render(request, 'clothes_a/children_clothes.html',
                      context=context_object_name)


def teenager_clothes(request):
    if request.method == "GET":
        query = models.Product.objects.filter(tags__name='для подростков').order_by('-id')
        context_object_name = {
            'teenager_clothes': query
        }
        return render(request, 'clothes_a/teenager_clothes.html',
                      context=context_object_name)


def adult_clothes(request):
    if request.method == "GET":
        query = models.Product.objects.filter(tags__name='для взрослых').order_by('-id')
        context_object_name = {
            'adult_clothes': query
        }
        return render(request, 'clothes_a/adult_clothes.html',
                      context=context_object_name)

