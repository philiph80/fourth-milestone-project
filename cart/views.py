from django.shortcuts import (render, redirect, reverse)
import json
from pizza_dojo.utils.decorators import select_store_decorator


@select_store_decorator
def view_cart(request):

    return render(request, 'cart/cart.html')


def add_to_cart(request, product_id):
    cart = request.session.get('cart', [])
    # Size_price is on each menu item mapping size to price
    size_price = json.loads(request.POST.get('size_price'))
    size = size_price['size']
    price = size_price['price']
    product_type = request.POST.get('product_type')
    quantity = int(request.POST.get('quantity'))
    customizations = request.POST.get('customizations')
    if product_type == 'PIZZA':
        cart.extend([{'product_id': product_id, 'size': size, 'item_price': price, 'quantity': 1, 'customizations': customizations}] * quantity)
        request.session['cart'] = cart
        return redirect(request.META.get('HTTP_REFERER'))

    if cart == []:
        cart.append({'product_id': product_id, 'size': size, 'item_price': price, 'quantity': quantity, 'customizations': customizations})
        request.session['cart'] = cart
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        for index, item in enumerate(cart):
            if (item['product_id'] == product_id) and (item['size'] == size):
                cart[index]['quantity'] += quantity
                request.session['cart'] = cart
                return redirect(request.META.get('HTTP_REFERER'))
    # Cart has items, but none are identical to the new item
    cart.append({'product_id': product_id, 'size': size, 'item_price': price, 'quantity': quantity, 'customizations': customizations})
    request.session['cart'] = cart
    return redirect(request.META.get('HTTP_REFERER'))


def adjust_cart(request, product_id):
    cart = request.session.get('cart', [])
    adjust_type = request.POST.get('adjust-type')
    product_type = request.POST.get('product-type')
    item_index = int(request.POST.get('item-index'))
    if adjust_type == 'remove':
        cart.pop(item_index)
        request.session['cart'] = cart
        return redirect(reverse('view_cart'))
    #For pizzas, rather than increasing quantity, 
    #the item is copied and appended to the list
    if (adjust_type == 'increase') and (product_type == 'PIZZA'):
        product = cart[item_index]
        cart.append(product)
        request.session['cart'] = cart
        return redirect(reverse('view_cart'))
    elif (adjust_type == 'increase'):
        cart[item_index]['quantity'] += 1
        request.session['cart'] = cart
        return redirect(reverse('view_cart'))

    if (adjust_type == 'decrease') and (product_type != 'PIZZA'):
        if cart[item_index]['quantity'] > 1:
            cart[item_index]['quantity'] -= 1
            request.session['cart'] = cart
        return redirect(reverse('view_cart'))
