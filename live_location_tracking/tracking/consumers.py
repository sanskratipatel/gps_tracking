# tracking/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import LocationLog

class LocationTrackingConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        if self.scope['user'].is_authenticated:
            self.room_group_name = f"user_{self.scope['user'].id}"

            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
            await self.accept()
        else:
            await self.close()

    async def disconnect(self, close_code):
        if self.scope['user'].is_authenticated:
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )

    async def receive(self, text_data):
        data = json.loads(text_data)
        latitude = data['latitude']
        longitude = data['longitude']

        LocationLog.objects.create(user=self.scope['user'], latitude=latitude, longitude=longitude)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'location_update',
                'latitude': latitude,
                'longitude': longitude
            }
        )

    async def location_update(self, event):
        await self.send(text_data=json.dumps(event))
