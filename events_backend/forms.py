# forms.py
from django import forms
from events_app.models import Event, EventCategory, EventRegion
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.forms.widgets import DateInput, TimeInput


#create events
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'location', 'date', 'registration_required', 'registration_link', 'category', 'Region', 'image', 'status']

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'Enter event title'
        self.fields['description'].widget.attrs['placeholder'] = 'Enter event description'
        self.fields['location'].widget.attrs['placeholder'] = 'Enter event location'
        self.fields['date'].widget.attrs['placeholder'] = 'Enter event date (YYYY-MM-DD HH:MM:SS)'
        self.fields['registration_link'].widget.attrs['placeholder'] = 'Enter registration link'

        # Set fields as required, excluding registration_required
        for field_name in self.fields:
            if field_name not in ['registration_required', 'registration_link']:
                self.fields[field_name].required = True
   

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
        
        
        
# User forms 

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            # Redirect the user to the login page after successful submission
            # return HttpResponseRedirect(reverse('backend:login'))  # Replace 'login' with your login URL name
        return user
    
    
#Search form
class EventSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, required=False)