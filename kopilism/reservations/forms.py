from django import forms
from .models import Reservation

TIME_CHOICES = [
    ('09:00', '09:00 AM'), ('10:00', '10:00 AM'), ('11:00', '11:00 AM'),
    ('12:00', '12:00 PM'), ('13:00', '01:00 PM'), ('14:00', '02:00 PM'),
    ('15:00', '03:00 PM'), ('16:00', '04:00 PM'), ('17:00', '05:00 PM'),
    ('18:00', '06:00 PM'), ('19:00', '07:00 PM'), ('20:00', '08:00 PM'),
]

GUEST_CHOICES = [(i, f'{i} guest{"s" if i > 1 else ""}') for i in range(1, 11)]


class ReservationForm(forms.ModelForm):
    time = forms.ChoiceField(choices=TIME_CHOICES)
    guests = forms.ChoiceField(choices=GUEST_CHOICES)

    class Meta:
        model = Reservation
        fields = ['full_name', 'phone', 'email', 'date', 'time', 'guests', 'special_requests']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'special_requests': forms.Textarea(attrs={'rows': 3}),
        }
