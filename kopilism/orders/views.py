import json
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from menu.models import MenuItem
from .models import Order, OrderItem


def order_checkout(request):
    """Render the checkout/payment page."""
    return render(request, 'orders/checkout.html')


@csrf_exempt
@require_POST
def place_order(request):
    """Accept JSON cart, create Order + OrderItems, return order id."""
    try:
        data = json.loads(request.body)
        cart = data.get('cart', [])
        payment_method = data.get('payment_method', 'cash')
        customer_name = data.get('customer_name', '')
        table_number = data.get('table_number', None)

        if not cart:
            return JsonResponse({'error': 'Cart is empty.'}, status=400)

        order = Order.objects.create(
            customer_name=customer_name,
            table_number=table_number,
            payment_method=payment_method,
            status='pending',
        )

        for entry in cart:
            menu_item = get_object_or_404(MenuItem, pk=entry['id'])
            OrderItem.objects.create(
                order=order,
                menu_item=menu_item,
                quantity=entry['quantity'],
                unit_price=menu_item.price,
            )

        order.calculate_total()
        return JsonResponse({'order_id': order.pk, 'total': str(order.total_amount)})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def order_ready(request, order_id):
    """Show 'food is ready' screen with receipt."""
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'orders/ready.html', {'order': order})


def order_status(request, order_id):
    """AJAX endpoint — poll order status."""
    order = get_object_or_404(Order, pk=order_id)
    return JsonResponse({'status': order.status, 'status_display': order.get_status_display()})


@csrf_exempt
@require_POST
def mark_ready(request, order_id):
    """Admin/staff endpoint to mark order as ready."""
    order = get_object_or_404(Order, pk=order_id)
    order.status = 'ready'
    order.save()
    return JsonResponse({'ok': True})
