from django.contrib import admin

from apps.tours.models import Tour

# Register your models here.
@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date', 'price')
    list_filter = ('title', 'description', 'date', 'price')