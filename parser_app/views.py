from django.shortcuts import render, redirect
from django.views import generic

from . import models, forms


class AnilibriaScheduleView(generic.ListView):
    template_name = 'parser_app/anilibria_schedule.html'
    context_object_name = 'schedule'
    model = models.AnilibriaModel

    def get_queryset(self):
        return self.model.objects.all().order_by('id')


class AnilibriaFormView(generic.FormView):
    template_name = 'parser_app/anilibria_form.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return redirect('anilibria_schedule')
        return super().post(request, *args, **kwargs)
