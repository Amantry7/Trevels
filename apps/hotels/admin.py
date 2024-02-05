from django.contrib import admin

from apps.hotels.models import Hotel

# Register your models here.
@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'tour')
    search_fields = ('title', 'description', 'tour__title')
    list_filter = ('tour', )