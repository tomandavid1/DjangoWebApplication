from django.shortcuts import render

# Views for base app

def home(request):
    return render(request, 'home.html')

def room(request):
    return render(request, 'room.html')