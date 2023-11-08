# forms.py
from django import forms
from events_app.models import Event, EventCategory, EventRegion


#Region form
class EventRegionForm(forms.ModelForm):
    class Meta:
        model = EventRegion
        fields = ['name']  
        


#category form
class EventCategoryForm(forms.ModelForm):
    class Meta:
        model = EventCategory
        fields = ['name']  

#update event form
class EventUpdateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'location', 'date', 'registration_required', 'registration_link', 'category', 'Region', 'image', 'status']

    
#update Category form
class CategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = EventCategory
        fields = ['name']
        
#update Region form
class RegionUpdateForm(forms.ModelForm):
    class Meta:
        model = EventRegion
        fields = ['name']