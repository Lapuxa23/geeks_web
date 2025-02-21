from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, RedirectView, View
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book, Order, OrderItem

class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'books_list.html'
    context_object_name = 'books'

class AddToCartView(LoginRequiredMixin, RedirectView):
    pattern_name = 'books_list'

    def get_redirect_url(self, *args, **kwargs):
        book = get_object_or_404(Book, id=kwargs['books_id'])
        order, created = Order.objects.get_or_create(user=self.request.user, status='Pending')
        order_item, created = OrderItem.objects.get_or_create(order=order, book=book, defaults={'price': book.price})

        if not created:
            order_item.quantity += 1
            order_item.save()

        order.total_price = sum(item.price * item.quantity for item in order.items.all())
        order.save()

        return super().get_redirect_url(*args, **kwargs)

class UpdateCartItemView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        item = get_object_or_404(OrderItem, id=kwargs['item_id'], order__user=request.user)
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0:
            item.quantity = quantity
            item.save()
        else:
            item.delete()

        order = item.order
        order.total_price = sum(item.price * item.quantity for item in order.items.all())
        order.save()

        return redirect('cart')

class RemoveFromCartView(LoginRequiredMixin, RedirectView):
    pattern_name = 'cart'

    def get_redirect_url(self, *args, **kwargs):
        item = get_object_or_404(OrderItem, id=kwargs['item_id'], order__user=self.request.user)
        order = item.order
        item.delete()

        order.total_price = sum(item.price * item.quantity for item in order.items.all())
        order.save()

        return super().get_redirect_url(*args, **kwargs)

class CartView(LoginRequiredMixin, ListView):
    model = OrderItem
    template_name = 'cart.html'
    context_object_name = 'order_items'

    def get_queryset(self):
        order = Order.objects.filter(user=self.request.user, status='Pending').first()
        return order.items.all() if order else []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = Order.objects.filter(user=self.request.user, status='Pending').first()
        context['order'] = order
        return context

class CheckoutView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        order = Order.objects.filter(user=request.user, status='Pending').first()
        if order:
            order.status = 'Completed'
            order.save()
            return render(request, 'checkout_success.html')
        return redirect('cart')