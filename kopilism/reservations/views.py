from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ReservationForm


def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reservation confirmed! We will reach out to confirm your booking.')
            return redirect('reservation_success')
    else:
        form = ReservationForm()
    return render(request, 'reservations/reservation.html', {'form': form})


def reservation_success(request):
    return render(request, 'reservations/success.html')
