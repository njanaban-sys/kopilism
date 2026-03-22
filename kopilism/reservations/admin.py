from django.contrib import admin
from .models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'date', 'time', 'guests', 'status', 'created_at']
    list_filter = ['status', 'date']
    list_editable = ['status']
    search_fields = ['full_name', 'phone', 'email']
    ordering = ['-date', '-time']
