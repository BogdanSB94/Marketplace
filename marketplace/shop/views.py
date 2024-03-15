from django.shortcuts import render, redirect
from item.models import Category, Item, CartItem
from .forms import SignupForm
from django.contrib.auth import logout as auth_logout


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'shop/index.html', {
        'categories': categories,
        'items': items,
    })


def contact(request):
    return render(request, 'shop/contact.html')


def add_to_cart(request, item_id):
    item = Item.objects.get(pk=item_id)
    user = request.user
    cart_item, created = CartItem.objects.get_or_create(user=user, item=item)

    if created:
        cart_item.quantity += 1
    else:
        cart_item.quantity += 1

    cart_item.save()
    return redirect('shop:view_cart')


def view_cart(request):
    cart_items = CartItem.objects.all()
    total = sum(item.subtotal() for item in cart_items)

    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        item_to_remove = CartItem.objects.get(id=item_id)
        item_to_remove.delete()
        return redirect('shop:view_cart')

    return render(request, 'shop/cart.html', {'cart_items': cart_items, 'total': total})


def purchase_complete(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)
    cart_items.delete()
    return render(request, 'shop/purchase_complete.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'shop/signup.html', {
        'form': form
    })


def logout(request):
    auth_logout(request)
    return redirect('shop:index')
