from django.shortcuts import render, redirect, get_object_or_404
from component.models import Component
from django.contrib import messages

def view_basket(request):
    basket = request.session.get('basket', {})
    components = []
    total = 0

    # Make a copy of keys to iterate safely while modifying session
    basket_keys = list(basket.keys())

    for comp_id_str in basket_keys:
        qty = basket[comp_id_str]
        try:
            comp_id = int(comp_id_str)
            comp = Component.objects.get(id=comp_id)
            components.append({
                'component': comp,
                'quantity': qty,
                'subtotal': comp.price * qty
            })
            total += comp.price * qty
        except Component.DoesNotExist:
            # Remove invalid component from basket
            basket.pop(comp_id_str)
            request.session['basket'] = basket
            messages.warning(
                request, "A component in your basket no longer exists and was removed.")

    return render(request, 'basket/view_basket.html', {
        'components': components,
        'total': total
    })

def add_to_basket(request, component_id):
    component = get_object_or_404(Component, id=component_id)
    
    basket = request.session.get('basket', {})

    # Increment quantity if already in basket
    if str(component.id) in basket:
        basket[str(component.id)] += 1
    else:
        basket[str(component.id)] = 1

    request.session["basket"] = basket
    messages.success(request, f"Added {component.name} to your basket.")
    return redirect(request.META.get('HTTP_REFERER', 'home'))   


def update_basket(request, component_id):
    if request.method == "POST":
        quantity = int(request.POST.get("quantity", 1))
        basket = request.session.get("basket", {})

        if quantity > 0:
            basket[str(component_id)] = quantity
        else:
            # Remove the item if quantity is 0
            basket.pop(str(component_id), None)

        request.session["basket"] = basket

    messages.success(request, 'Basket updated successfully.')
    return redirect("basket:view_basket")

def remove_from_basket(request, component_id):
    basket = request.session.get('basket', {})
    basket.pop(str(component_id), None)
    request.session['basket'] = basket
    messages.success(request, 'Item removed from basket.')
    return redirect('basket:view_basket')