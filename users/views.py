from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib import messages
from . import models, forms

class RegisterView(CreateView):
    form_class = forms.CustomRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        messages.success(self.request, 'Регистрация прошла успешно!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Ошибка при регистрации. Проверьте данные.')
        return super().form_invalid(form)

class AuthLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'

    def form_valid(self, form):
        messages.success(self.request, 'Вы успешно вошли в систему.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Неверный логин или пароль.')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse('users:user_list')

class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('users:login')

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, 'Вы вышли из системы.')
        return super().dispatch(request, *args, **kwargs)

class UserListView(ListView):
    template_name = 'users/user_list.html'
    context_object_name = 'users'
    model = models.CustomUser
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('search', '')
        return models.CustomUser.objects.filter(username__icontains=query)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        return context
