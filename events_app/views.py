from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import EventCategory, EventRegion, Event
from django.utils.text import slugify
# from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
class HomeListView(ListView):
    model = Event
    template_name = 'events_app/home.html'
    context_object_name = 'events'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = EventCategory.objects.all()
        return context

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

# # User Registrations View
# def register_request(request):
# 	if request.method == "POST":
# 		form = NewUserForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			login(request, user)
# 			messages.success(request, "Registration successful." )
# 			return redirect("event:index")
# 		messages.error(request, "Unsuccessful registration. Invalid information.")
# 	form = NewUserForm()
# 	return render (request=request, template_name="events_app/register.html", context={"register_form":form})  

# # User login View
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib import messages

# def login_request(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.info(request, f"You are now logged in as {username}.")
#                 # Redirect to the "dashboard" view within the "events_backend" namespace
#                 return redirect("events_backend:home")
#             else:
#                 messages.error(request, "Invalid username or password.")
#         else:
#             messages.error(request, "Invalid username or password.")
#     form = AuthenticationForm()
#     return render(request=request, template_name="events_app/login.html", context={"login_form": form})


# # User logout View
# def logout_request(request):
# 	logout(request)
# 	messages.info(request, "You have successfully logged out.") 
# 	return redirect("events_app:index")