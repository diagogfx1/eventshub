# forms.py
from django import forms
from events_app.models import Event, EventCategory, EventRegion, UserProfile
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
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
        
        # Increase space for description by using a Textarea widget with a fixed height
        self.fields['description'].widget = forms.Textarea(attrs={'placeholder': 'Enter event description', 'style': 'height: 200px;'})

        self.fields['location'].widget.attrs['placeholder'] = 'Enter event location'
        
        # Use DateTimeInput widget for the 'date' field to add a date and time picker
        self.fields['date'].widget = forms.DateTimeInput(attrs={'placeholder': 'Enter event date and time (YYYY-MM-DD HH:MM:SS)', 'type': 'datetime-local'})
        
        self.fields['registration_link'].widget.attrs['placeholder'] = 'Enter registration link'

        # Rename the 'date' field label to 'Date & Time'
        self.fields['date'].label = 'Date & Time'
        
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
    
    def __init__(self, *args, **kwargs):
        super(EventUpdateForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'Enter event title'
        
        # Increase space for description by using a Textarea widget with a fixed height
        self.fields['description'].widget = forms.Textarea(attrs={'placeholder': 'Enter event description', 'style': 'height: 200px;'})

        self.fields['location'].widget.attrs['placeholder'] = 'Enter event location'
        
        # Use DateTimeInput widget for the 'date' field to add a date and time picker
        self.fields['date'].widget = forms.DateTimeInput(attrs={'placeholder': 'Enter event date and time (YYYY-MM-DD HH:MM:SS)', 'type': 'datetime-local'})
        
        self.fields['registration_link'].widget.attrs['placeholder'] = 'Enter registration link'

        # Rename the 'date' field label to 'Date & Time'
        self.fields['date'].label = 'Date & Time'
        
        # Set fields as required, excluding registration_required
        for field_name in self.fields:
            if field_name not in ['registration_required', 'registration_link']:
                self.fields[field_name].required = True
    

    
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
    
# edit Profile form
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'first_name', 'last_name', 'phone_number', 'email']

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['avatar'].widget.attrs['class'] = 'form-control'  # Add CSS classes if needed
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['phone_number'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        
# change password form      
class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User()  # Use the user model you're using in your project

    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)

        # You can add custom field attributes or labels if needed. For example:
        self.fields['old_password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Old Password'})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'New Password'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm New Password'})
    
    
#Search form
class EventSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, required=False)
    