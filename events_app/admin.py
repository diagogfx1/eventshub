from django.contrib import admin
from .models import Event, EventCategory, EventRegion

# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "Region", "status", "created_at", "updated_at", "user")

@admin.register(EventCategory)
class EventCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(EventRegion)
class EventRegionAdmin(admin.ModelAdmin):
    pass
