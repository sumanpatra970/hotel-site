from django.urls import path

from travel_app import views

urlpatterns=[
    path('', views.index),
    path('login', views.login),
    path('signup', views.signup),
    path('login_next', views.login_next),
    path('signup_next', views.signup_next),
    path('booking', views.booking),
    path('gallery', views.gallery),
    path('About', views.about),
    path('bookingform', views.bookingform),
    path('offer1', views.offer_1),
    path('offer2', views.offer_2),
    path('feedback', views.feedback),
    path('completeform', views.completeform),
    path('working', views.account),
    path('accountdetail',views.account_final)
]