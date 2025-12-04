from django.shortcuts import render, redirect, get_object_or_404
from component.models import Component

def add_to_basket(request, component_id):
    component = get_object_or_404(Component, id=component_id)
    
    basket = request.session.get('basket', {})

    # Increment quantity if already in basket
    if str(component.id) in basket:
        basket[str(component.id)] += 1
    else:
        basket[str(component.id)] = 1

    request.session['basket'] = basket
    return redirect(request.META.get('HTTP_REFERER', 'home'))  # redirect back to page

def view_basket(request):
    basket = request.session.get('basket', {})
    components = []
    total = 0

    for comp_id, qty in basket.items():
        comp = get_object_or_404(Component, id=comp_id)
        components.append({
            'component': comp,
            'quantity': qty,
            'subtotal': comp.price * qty
        })
        total += comp.price * qty

    return render(request, 'basket/view_basket.html', {'components': components, 'total': total})
