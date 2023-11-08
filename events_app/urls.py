from django.urls import path
from . import views
from .views import (
    EventListView,
    EventDetailView,
    EventCreateView,
    EventUpdateView,
    EventDeleteView,
    EventCategoryListView,
    EventRegionListView,
    HomeListView,
    
)

urlpatterns = [
    path('', HomeListView.as_view(), name='index'),
    path('events/', EventListView.as_view(), name='event-list'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('events/create/', EventCreateView.as_view(), name='event-create'),
    path('events/<int:pk>/update/', EventUpdateView.as_view(), name='event-update'),
    path('events/<int:pk>/delete/', EventDeleteView.as_view(), name='event-delete'),
    path('event-categories/', EventCategoryListView.as_view(), name='event-category-list'),
    path('event-regions/', EventRegionListView.as_view(), name='event-region-list'),
    path('contact/', views.contact, name='contact'),
    path('event-categories/<int:category_id>/', views.events_by_category, name='events_by_category'),
    # path("register", views.register_request, name="register"),
    
    
]
