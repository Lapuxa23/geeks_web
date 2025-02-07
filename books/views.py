from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from . import models


def time_now(request):
    if request.method == 'GET':
        now = timezone.now()
        return HttpResponse(f'Current time: {now}')


def book_list_view(request):
    if request.method == 'GET':
        book = models.BookModel.objects.all().order_by('-id')
        context = {'book': book}
        return render(request, 'book.html', context)


def text_photo(request):
    return HttpResponse('Фотография отсутствует')


def about_me(request):
    if request.method == 'GET':
        return HttpResponse('Я Эсенбеков Тимур Эсенбекович')
