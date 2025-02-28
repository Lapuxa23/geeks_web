from django.views.generic import TemplateView, ListView, DetailView
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render
from .models import BookModel


class TimeNowView(TemplateView):
    def get(self, request, *args, **kwargs):
        now = timezone.now()
        return HttpResponse(f'Current time: {now}')


class BookListView(ListView):
    model = BookModel
    template_name = 'book.html'
    context_object_name = 'books'
    from django.views.generic import TemplateView, ListView, DetailView


from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render
from django.core.cache import cache
from .models import BookModel


class TimeNowView(TemplateView):
    def get(self, request, *args, **kwargs):

=
cache.clear()

now = timezone.now()
return HttpResponse(f'Current time: {now}')


class BookListView(ListView):
    model = BookModel
    template_name = 'book.html'
    context_object_name = 'books'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return BookModel.objects.filter(title__icontains=query).order_by('-id')
        return BookModel.objects.all().order_by('-id')


class TextPhotoView(TemplateView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Фотография отсутствует')


class AboutMeView(TemplateView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Я Эсенбеков Тимур Эсенбекович')

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return BookModel.objects.filter(title__icontains=query).order_by('-id')
        return BookModel.objects.all().order_by('-id')


class TextPhotoView(TemplateView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Фотография отсутствует')


class AboutMeView(TemplateView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Я Эсенбеков Тимур Эсенбекович')
