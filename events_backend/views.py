from django.shortcuts import render,redirect  
from events_app.models import Event, EventCategory, EventRegion
from django.urls import reverse_lazy
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .forms import EventRegionForm, EventCategoryForm, EventUpdateForm, CategoryUpdateForm, RegionUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.

#dashboard
def dashboard(request):
    return render(request, 'events_backend/dashboard.html')

# Event List View
class EventListView(ListView):
    model = Event
    template_name = 'events_backend/dashboard.html'
    context_object_name = 'events'
    paginate_by = 10
    
# All Event List
class AllEvents(ListView):
    model = Event
    template_name = 'events_backend/all_events.html'
    context_object_name = 'events'
    paginate_by = 10

# Event Create View
class EventCreateView(CreateView):
    model = Event
    template_name = 'events_backend/event_form.html'
    fields = ['title', 'description', 'location', 'date', 'registration_required', 'registration_link', 'category', 'Region', 'image', 'status']
    def get_form(self, form_class=None):
        form = super(EventCreateView, self).get_form(form_class)
        helper = FormHelper()
        helper.form_method = 'post'
        helper.add_input(Submit('submit', 'Create Event'))
        form.helper = helper
        return form
    success_url = reverse_lazy('backend:home')  # Replace with the actual view name

# Event Update View
class EventUpdateView(UpdateView):
    model = Event
    template_name = 'events_backend/edit_event.html'
    form_class = EventUpdateForm  # Use the EventUpdateForm we defined
    success_url = reverse_lazy('backend:home')  # Replace with the URL where you want to redirect after updating
    
    
# Categorry Update View
class CategoryUpdateView(UpdateView):
    model = EventCategory
    template_name = 'events_backend/edit_category.html'
    form_class = CategoryUpdateForm  
    success_url = reverse_lazy('backend:view-categories')  
    
# Region Update View
class RegionUpdateView(UpdateView):
    model = EventCategory
    template_name = 'events_backend/edit_region.html'
    form_class = RegionUpdateForm  
    success_url = reverse_lazy('backend:view-region')  
    
    
    

# Event Delete View
class EventDeleteView(DeleteView):
    model = Event
    template_name = 'events_backend/delete_event.html'
    success_url = reverse_lazy('backend:view-categories')
    
    
# Category Delete View
class CategoryDeleteView(DeleteView):
    model = EventCategory
    template_name = 'events_backend/delete_category.html'
    success_url = reverse_lazy('backend:view-categories')
    
    
# Region Delete View
class RegionDeleteView(DeleteView):
    model = EventRegion
    template_name = 'events_backend/delete_region.html'
    success_url = reverse_lazy('backend:view-region')
    
# Event Region List View
class EventRegionListView(ListView):
    model = EventRegion
    template_name = 'events_backend/region_list.html'
    context_object_name = 'regions'
    
# Event Category List View
# @login_required
# class CategoryList(ListView):
#     model = EventCategory
#     template_name = 'events_backend/category_list.html'
#     context_object_name = 'categorys'


# Event Category List View
def category_list(request):
    categories = EventCategory.objects.all()
    context = {
        'categorys': categories,
    }
    return render(request, 'events_backend/category_list.html', context)


#create region
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
def create_category(request):
    if request.method == 'POST':
        form = EventCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('backend:view-categories'))   # Redirect to the region list view  # Redirect to the region list view
    else:
        form = EventCategoryForm()
    return render(request, 'events_backend/category_form.html', {'form': form})
    