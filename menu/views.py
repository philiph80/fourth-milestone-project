from django.shortcuts import render, redirect
from .models import Product, Topping, ToppingAmount
from pizza_dojo.utils.decorators import select_store_decorator


@select_store_decorator
def menu(request):
    pizza_list = []
    side_list = []
    dessert_list = []
    drink_list = []
    all_products = Product.objects.order_by('position')
    for product in all_products:
        menu_item = {
            'product': None,
            'sizes': [],

        }
        if product.product_type == 'PIZZA':
            sizes = []
            if product.small_price:
                sizes.append({'price': str(product.small_price),
                              'size': 'Small'})
            if product.regular_price:
                sizes.append({'price': str(product.regular_price),
                              'size': 'Regular'})
            if product.large_price:
                sizes.append({'price': str(product.large_price),
                              'size': 'Large'})
            menu_item['product'] = product
            menu_item['sizes'] = sizes
            pizza_toppings = []
            for top_amt in product.topping_amounts.all():
                pizza_toppings.append(
                    (top_amt.topping.name, top_amt.get_amount_display()))
            menu_item['toppings'] = pizza_toppings
            pizza_list.append(menu_item)

        if product.product_type == 'SIDE':
            sizes = []
            if product.small_price:
                sizes.append({'price': str(product.small_price),
                              'size': 'Small'})
            if product.regular_price:
                sizes.append({'price': str(product.regular_price),
                              'size': 'Regular'})
            if product.large_price:
                sizes.append({'price': str(product.large_price),
                              'size': 'Large'})
            menu_item['product'] = product
            menu_item['sizes'] = sizes
            side_list.append(menu_item)

        if product.product_type == 'DESSERT':
            sizes = []
            if product.small_price:
                sizes.append({'price': str(product.small_price),
                              'size': 'Small'})
            if product.regular_price:
                sizes.append({'price': str(product.regular_price),
                              'size': 'Regular'})
            if product.large_price:
                sizes.append({'price': str(product.large_price),
                              'size': 'Large'})
            menu_item['product'] = product
            menu_item['sizes'] = sizes
            dessert_list.append(menu_item)

        if product.product_type == 'DRINK':
            sizes = []
            if product.small_price:
                sizes.append({'price': str(product.small_price),
                              'size': 'Small'})
            if product.regular_price:
                sizes.append({'price': str(product.regular_price),
                              'size': 'Regular'})
            if product.large_price:
                sizes.append({'price': str(product.large_price),
                              'size': 'Large'})
            menu_item['product'] = product
            menu_item['sizes'] = sizes
            drink_list.append(menu_item)

    context = {
        'pizzas': pizza_list,
        'sides': side_list,
        'desserts': dessert_list,
        'drinks': drink_list,
    }
    return render(request, 'menu/menu.html', context)


def flush_session(request):
    request.session.flush()
    return redirect('menu')
