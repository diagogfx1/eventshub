# forms.py
from django import forms
from events_app.models import Event, EventCategory, EventRegion
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse



#create events
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'location', 'date', 'registration_required', 'registration_link', 'category', 'Region', 'image', 'status']

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