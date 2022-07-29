import requests
from django.shortcuts import render
from .models import Position


def home_view(request):
    """View that gets data from the API and shows it on template"""

    data = Position.objects.all()

    context = {'data': data}
    return render(request, 'positions/main.html', context)
