from django.shortcuts import render
from .models import Category, MenuItem


def home(request):
    categories = Category.objects.prefetch_related('items').all()
    active_category = categories.first()
    context = {
        'categories': categories,
        'active_category': active_category,
    }
    return render(request, 'menu/home.html', context)


def menu(request):
    categories = Category.objects.prefetch_related('items').all()
    active_slug = request.GET.get('category', 'coffee')
    active_category = Category.objects.filter(slug=active_slug).first() or categories.first()
    items = MenuItem.objects.filter(category=active_category, is_available=True)
    context = {
        'categories': categories,
        'active_category': active_category,
        'items': items,
    }
    return render(request, 'menu/menu.html', context)
