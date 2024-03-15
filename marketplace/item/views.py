from django.shortcuts import render, get_object_or_404
from .models import Item, Category, CartItem


def browse(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    browse = Item.objects.filter(is_sold=False)

    if category_id:
        browse = browse.filter(category_id=category_id)

    if query:
        browse = browse.filter(name__icontains=query)

    return render(request, 'item/browse.html', {
        'browse': browse,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
    })


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items
    })


def view_cart(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)
    total = sum(item.subtotal() for item in cart_items)
    return render(request, 'shop/cart.html', {'cart_items': cart_items, 'total': total})
