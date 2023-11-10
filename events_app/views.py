from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import EventCategory, EventRegion, Event
from django.utils.text import slugify
from django import forms
from .forms import EventSearchForm
from django.contrib.auth import login, authenticate, logout 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



# Create your views here.
# Home Event View
class HomeListView(ListView):
    model = Event
    template_name = 'events_app/home.html'
    context_object_name = 'events'
    paginate_by = 10

    def get_queryset(self):
        queryset = Event.objects.all()
        search_form = EventSearchForm(self.request.GET)
        if search_form.is_valid():
            query = search_form.cleaned_data.get('query')
            if query:
                queryset = queryset.filter(title__icontains=query) | queryset.filter(description__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = EventCategory.objects.all()
        context['search_form'] = EventSearchForm(self.request.GET)
        return context

# Event List View
class EventListView(ListView):
    model = Event
    template_name = 'events_app/event_list.html'
    context_object_name = 'events'
    paginate_by = 32
    ordering = ['date']

    def get_queryset(self):
        queryset = Event.objects.all().order_by('date')
        search_form = EventSearchForm(self.request.GET)
        if search_form.is_valid():
            query = search_form.cleaned_data.get('query')
            if query:
                queryset = queryset.filter(title__icontains=query) | queryset.filter(description__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        events = context['events']

        paginator = Paginator(events, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            events_paginated = paginator.page(page)
        except PageNotAnInteger:
            events_paginated = paginator.page(1)
        except EmptyPage:
            events_paginated = paginator.page(paginator.num_pages)

        context['events'] = events_paginated
        context['search_form'] = EventSearchForm(self.request.GET)
        return context
    
    
    
    

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

    
#Contact View
def contact(request):
    return render(request, 'events_app/contact.html')

# Event Region List View
class EventRegionListView(ListView):
    model = EventRegion
    template_name = 'events_app/eventregion_list.html'
    context_object_name = 'regions'
    
# Event Category List View
class EventCategoryListView(ListView):
    model = EventCategory
    template_name = 'events_app/eventcategory_list.html,'
    context_object_name = 'categories'

    
# display events under event EventCategory
def events_by_category(request, category_id):
    category = get_object_or_404(EventCategory, id=category_id)
    events = Event.objects.filter(category=category)
    context = {
        'category': category,
        'events': events,
    }
    return render(request, 'events_app/events_by_category.html', context)


# Event Search View
def event_search(request):
    form = EventSearchForm(request.GET)
    events = []

    if form.is_valid():
        query = form.cleaned_data.get('query')
        # Customize the search criteria based on your requirements
        events = Event.objects.filter(title__icontains=query)

    return render(request, 'events_app/event_search_results.html', {'form': form, 'events': events})
