from asgiref.sync import async_to_sync

from celery import shared_task

from channels.layers import get_channel_layer

import requests

from .models import Position


@shared_task
def get_crypto_data():
    """
    Get data from the API,
    store it in DB,
    send a message to the consumer to update it in realtime
    """

    # Get data
    url = (
        "https://api.coingecko.com/api/v3/coins/"
        "markets?vs_currency=USD&order=market_cap_desc&"
        "per_page=100&page=1&sparkline=false"
    )
    data = requests.get(url).json()

    # Delete old data
    Position.objects.all().delete()

    # Store new data
    for item in data:
        p, _ = Position.objects.get_or_create(name=item["name"])
        p.image = item["image"]
        p.price = item["current_price"]
        p.rank = item["market_cap_rank"]
        p.market_cap = item["market_cap"]
        p.save()

    # Send a message to the consumer
    channel_layer = get_channel_layer()
    message = {
        "type": "loc_message",
        "positions": "1",
    }
    async_to_sync(channel_layer.group_send)("realtime-data", message)
