from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.order_checkout, name='order_checkout'),
    path('place/', views.place_order, name='place_order'),
    path('ready/<int:order_id>/', views.order_ready, name='order_ready'),
    path('status/<int:order_id>/', views.order_status, name='order_status'),
    path('mark-ready/<int:order_id>/', views.mark_ready, name='mark_ready'),
]
