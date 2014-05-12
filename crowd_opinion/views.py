from django.shortcuts import render

def home(request):
    return render(request, 'crowd-opinion-home.html')
