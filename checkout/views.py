from django.shortcuts import render


def index(request):
    return render(request,'checkout/shipping-address.html')
# Create your views here.
