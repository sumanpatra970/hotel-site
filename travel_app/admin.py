from django.contrib import admin

from travel_app.models import bookings

class booking_details(admin.ModelAdmin):
    list_display = ['user','phoneno','date','room','price','city']

admin.site.register(bookings,booking_details)