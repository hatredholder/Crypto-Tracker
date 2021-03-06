import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from .models import Position


class PositionConsumer(WebsocketConsumer):
    """Basic websocket consumer"""

    def connect(self):
        self.channel_group_name = 'realtime-data'
        
        # Create a group called 'realtime-data'
        async_to_sync(self.channel_layer.group_add)(
            self.channel_group_name,
            self.channel_name,
        )
        print("joined the group")

        self.accept()

    def disconnect(self, close_code):
        # Leave the group
        async_to_sync(self.channel_layer.group_discard)(
            self.channel_group_name,
            self.channel_name,
        )
        print("left the group")
        
    def loc_message(self, event):
        # Get new data from the DB
        for i in Position.objects.all():
            self.send(json.dumps({i.name:i.price}))