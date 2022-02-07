from django.shortcuts import render

def first(request):
    return render(request, 'travel_vechicle/vechicle_order.html')

def order(request):
    return render(request, 'travel_vechicle/order.html')