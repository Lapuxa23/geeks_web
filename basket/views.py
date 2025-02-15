from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, Order, OrderItem


@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    order, created = Order.objects.get_or_create(user=request.user, status='Pending')
    order_item, created = OrderItem.objects.get_or_create(order=order, book=book, defaults={'price': book.price})

    if not created:
        order_item.quantity += 1
        order_item.save()

    order.total_price = sum(item.price * item.quantity for item in order.items.all())
    order.save()

    return redirect('book_list')


@login_required
def update_cart_item(request, item_id):
    item = get_object_or_404(OrderItem, id=item_id, order__user=request.user)
    if request.method == 'POST':
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


@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(OrderItem, id=item_id, order__user=request.user)
    order = item.order
    item.delete()

    # Обновляем общую стоимость заказа
    order.total_price = sum(item.price * item.quantity for item in order.items.all())
    order.save()

    return redirect('cart')


@login_required
def cart(request):
    order = Order.objects.filter(user=request.user, status='Pending').first()
    return render(request, 'cart.html', {'order': order})


@login_required
def checkout(request):
    order = Order.objects.filter(user=request.user, status='Pending').first()
    if order:
        order.status = 'Completed'
        order.save()
        return render(request, 'checkout_success.html')
    return redirect('cart')
