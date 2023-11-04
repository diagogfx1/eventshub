from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import EventCategory, EventRegion, Event

# Create your views here.

# def home(request):
#     return render(request, 'events_app/home.html')

# HomeEvent List View
class HomeListView(ListView):
    model = Event
    template_name = 'events_app/home.html'
    context_object_name = 'events'
    paginate_by = 10



# Event List View
class EventListView(ListView):
    model = Event
    template_name = 'events_app/event_list.html'
    context_object_name = 'events'
    paginate_by = 10

# Event Detail View
class EventDetailView(DetailView):
    model = Event
    template_name = 'events_app/event_detail.html'
    context_object_name = 'event'

# Event Create View
class EventCreateView(CreateView):
    model = Event
    template_name = 'events_app/event_form.html'
    fields = ['title', 'description', 'location', 'date', 'registration_required', 'registration_link', 'category', 'Region', 'image', 'status']

# Event Update View
class EventUpdateView(UpdateView):
    model = Event
    template_name = 'events_app/event_form.html'
    fields = ['title', 'description', 'location', 'date', 'registration_required', 'registration_link', 'category', 'Region', 'image', 'status']

# Event Delete View
class EventDeleteView(DeleteView):
    model = Event
    template_name = 'events_app/event_confirm_delete.html'
    success_url = reverse_lazy('event-list')

# Event Category List View
class EventCategoryListView(ListView):
    model = EventCategory
    template_name = 'events_app/eventcategory_list.html'
    context_object_name = 'categories'

# Event Region List View
class EventRegionListView(ListView):
    model = EventRegion
    template_name = 'events_app/eventregion_list.html'
    context_object_name = 'regions'


def contact(request):
    return render(request, 'events_app/contact.html')