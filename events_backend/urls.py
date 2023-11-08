from django.urls import path
from . import views 
from .views import (
    EventListView,
    AllEvents,
    EventCreateView,
    EventUpdateView,
    EventDeleteView,
    # CategoryList,
    EventRegionListView,
    category_list
    
    
    
    
)


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('events/', EventListView.as_view(), name='home'),
    path('all_events/', AllEvents.as_view(), name='view-events'),
    path('events/create/', EventCreateView.as_view(), name='event-create'),
    path('events/<int:pk>/update/', EventUpdateView.as_view(), name='event-update'),
    path('events/<int:pk>/delete/', EventDeleteView.as_view(), name='event-delete'),
    path('create_region/', views.create_region, name='create-region'),
    path('create_category/', views.create_category, name='create-category'),
    # path('view_category/', CategoryList.as_view(), name='category-list'),
    path('view_region/', EventRegionListView.as_view(), name='view-region'),
    path('view_category/', category_list, name='view-categories'),
    path('update_event/<int:pk>/', EventUpdateView.as_view(), name='update-event'),
       
]