import requests
from celery import shared_task
from crypto_proj.celery import app

from .models import Position
from .utils import get_random_code


@shared_task
def get_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false"
    data = requests.get(url).json()

    for item in data:
        p, _ = Position.objects.get_or_create(name=item['name'])
        p.image = item['image']
        p.price = item['current_price']
        p.rank = item['market_cap_rank']
        p.market_cap = item['market_cap']
        p.save()

# @shared_task
# def create_test_object(name):
#     Test.objects.create(name=name)

# @shared_task
# def create_all_codes():
#     for test in Test.objects.all():
#         test.code = get_random_code()
#         test.save()

# @app.task
# def run_create_obj():
#     create_test_object.delay(name='new2022')

