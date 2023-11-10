from django.urls import path
from . import views 
from .views import (
    EventListView,
    AllEvents,
    EventCreateView,
    EventUpdateView,
    EventDeleteView,
    CategoryDeleteView,
    # CategoryList,
    EventRegionListView,
    category_list,
    CategoryUpdateView,
    RegionUpdateView,
    RegionDeleteView,
    event_search,
    
    
    
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
    path('update_category/<int:pk>/', CategoryUpdateView.as_view(), name='update-category'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
    path('update_regions/<int:pk>/', RegionUpdateView.as_view(), name='update-regions'),
    path('regions/<int:pk>/delete/', RegionDeleteView.as_view(), name='region-delete'),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path("register", views.register_request, name="register"),
    path('search/', event_search, name='event_search'),
       
]