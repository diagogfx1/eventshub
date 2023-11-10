from django.shortcuts import render, redirect  
from events_app.models import Event, EventCategory, EventRegion
from django.urls import reverse_lazy
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .forms import EventRegionForm, EventCategoryForm, EventUpdateForm, CategoryUpdateForm, RegionUpdateForm, EventForm, EventSearchForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, authenticate, logout 
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm
from django.contrib import messages
from django.core.exceptions import PermissionDenied

# Create your views here.

# Views required login
class LoginRequiredMixin:
    @classmethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        return login_required(view)
    
    
#dashboard
def dashboard(request):
    return render(request, 'events_backend/dashboard.html')

# Event List View
class EventListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'events_backend/dashboard.html'
    context_object_name = 'events'
    paginate_by = 30
    
    def get_queryset(self):
        # Filter events based on the logged-in user
        return Event.objects.filter(user=self.request.user).order_by('-created_at')
    
# All Event List
class AllEvents(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'events_backend/all_events.html'
    context_object_name = 'events'
    paginate_by = 10
    
    def get_queryset(self):
        # Filter events based on the logged-in user
        return Event.objects.filter(user=self.request.user).order_by('-created_at')

# Crete Event View
class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    template_name = 'events_backend/event_form.html'
    form_class = EventForm
    success_url = reverse_lazy('backend:view-events')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



# Event Update View
class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    template_name = 'events_backend/edit_event.html'
    form_class = EventUpdateForm  # Use the EventUpdateForm we defined
    success_url = reverse_lazy('backend:view-events')  # Replace with the URL where you want to redirect after updating
    
    
# Categorry Update View
class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = EventCategory
    template_name = 'events_backend/edit_category.html'
    form_class = CategoryUpdateForm  
    success_url = reverse_lazy('backend:view-categories')  
    
# Region Update View
class RegionUpdateView(LoginRequiredMixin, UpdateView):
    model = EventRegion
    template_name = 'events_backend/edit_region.html'
    form_class = RegionUpdateForm  
    success_url = reverse_lazy('backend:view-region')  
    
    
    

# Event Delete View
class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    template_name = 'events_backend/delete_event.html'
    success_url = reverse_lazy('backend:view-events')
    
    
# Category Delete View
class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = EventCategory
    template_name = 'events_backend/delete_category.html'
    success_url = reverse_lazy('backend:view-categories')
    
    
# Region Delete View
class RegionDeleteView(LoginRequiredMixin, DeleteView):
    model = EventRegion
    template_name = 'events_backend/delete_region.html'
    success_url = reverse_lazy('backend:view-region')
    
# Event Region List View

class EventRegionListView(LoginRequiredMixin, ListView):
    model = EventRegion
    template_name = 'events_backend/region_list.html'
    context_object_name = 'regions'
    
    

# Event Category List View
@login_required
def category_list(request):
    categories = EventCategory.objects.all()
    context = {
        'categorys': categories,
    }
    return render(request, 'events_backend/category_list.html', context)


#create region
@login_required
def create_region(request):
    if request.method == 'POST':
        form = EventRegionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('backend:view-region'))  # Redirect to the region list view
    else:
        form = EventRegionForm()
    return render(request, 'events_backend/region_form.html', {'form': form})



#create Category
@login_required
def create_category(request):
    if request.method == 'POST':
        form = EventCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('backend:view-categories'))   # Redirect to the region list view  # Redirect to the region list view
    else:
        form = EventCategoryForm()
    return render(request, 'events_backend/category_form.html', {'form': form})



# User Registrations View
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("backend:login")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = NewUserForm()

    return render(request=request, template_name="events_app/register.html", context={"register_form": form})


# User login View
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("events_backend:home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        # Set placeholders for the login form
        form = AuthenticationForm()
        form.fields['username'].widget.attrs['placeholder'] = 'Enter your username'
        form.fields['password'].widget.attrs['placeholder'] = 'Enter your password'

    return render(request=request, template_name="events_app/login.html", context={"login_form": form})


# User logout View
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
  
	return redirect("index")


# Event Search View
def event_search(request):
    form = EventSearchForm(request.GET)
    events = []

    if form.is_valid():
        query = form.cleaned_data.get('query')
        # Customize the search criteria based on your requirements
        events = Event.objects.filter(title__icontains=query)

    return render(request, 'events_backend/event_search_results.html', {'form': form, 'events': events})
    
    
