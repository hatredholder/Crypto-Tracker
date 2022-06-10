import json

from channels.generic.websocket import WebsocketConsumer

from .models import Position


class PositionConsumer(WebsocketConsumer):

    def connect(self):

        self.accept()

        for i in Position.objects.all():
            self.send(json.dumps({i.name:i.price}))
