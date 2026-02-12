from django.contrib import admin
from .models import Place, Route, Review


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'latitude', 'longitude']
    search_fields = ['name', 'address', 'description']
    list_filter = ['name']


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ['title', 'duration_hours', 'difficulty', 'created_at']
    list_filter = ['difficulty', 'created_at']
    search_fields = ['title', 'description']
    filter_horizontal = ['places']
    date_hierarchy = 'created_at'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'route', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['user__username', 'route__title', 'comment']
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at']