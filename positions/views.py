import requests
from django.shortcuts import render


def home_view(request):
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false"
    data = requests.get(url).json()

    context = {'data': data}

    return render(request, 'positions/main.html', context)
