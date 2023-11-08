# forms.py
from django import forms
from events_app.models import Event, EventCategory, EventRegion


#Region form
class EventRegionForm(forms.ModelForm):
    class Meta:
        model = EventRegion
        fields = ['name']  # Include the fields you want to capture


#category form
class EventCategoryForm(forms.ModelForm):
    class Meta:
        model = EventCategory
        fields = ['name']  # Include the fields you want to capture

#update event form
class EventUpdateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'location', 'date', 'registration_required', 'registration_link', 'category', 'Region', 'image', 'status']

    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        'location': forms.TextInput(attrs={'class': 'form-control'}),
        'date': forms.DateInput(attrs={'class': 'form-control datepicker'}),
        'registration_required': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'registration_link': forms.URLInput(attrs={'class': 'form-control'}),
        'category': forms.Select(attrs={'class': 'form-control'}),
        'Region': forms.Select(attrs={'class': 'form-control'}),
        'image': forms.FileInput(attrs={'class': 'form-control'}),
        'status': forms.Select(attrs={'class': 'form-control'}),
    }