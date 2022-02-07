from django.contrib import admin

from django.urls import path, include

from travel_vechicle import url

from travel_app import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(urls)),
    path('vechicle/',include(url)),
]
