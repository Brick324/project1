from django.shortcuts import render

def index(request):
    return render(request, "main/index.html")

def themes(request):
    return render(request, "main/themes.html")

def vehicles(request):
    return render(request, "main/vehicles.html")

def test(request):
    return render(request, "main/test.html")



# Create your views here.
