from django.urls import path
from travel_vechicle import views

urlpatterns=[
    path('placeorder',views.first),
    path('order',views.order)
]