from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Order, OrderItem


def book_list(request):
    books = Book.objects.all()
    return render(request, 'combined_template.html', {
        'template': 'book_list',
        'books': books,
    })


def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    order, created = Order.objects.get_or_create(user=request.user, status='Pending')
    order_item, created = OrderItem.objects.get_or_create(order=order, book=book)
    if not created:
        order_item.quantity += 1
        order_item.save()
    return redirect('book_list')


def cart(request):
    order = Order.objects.filter(user=request.user, status='Pending').first()
    return render(request, 'combined_template.html', {
        'template': 'cart',
        'order': order,
    })


def checkout(request):
    order = Order.objects.filter(user=request.user, status='Pending').first()
    if order:
        order.status = 'Completed'
        order.save()
        return render(request, 'combined_template.html', {
            'template': 'checkout_success',
        })
    return redirect('cart')
