from django.shortcuts import render

# Create your views here.


def Portfolio_link(request):
    return render(request, 'index.html')
