import json
from channels.generic.websocket import AsyncWebsocketConsumer

class StandingsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.contest_id = self.scope['url_route']['kwargs']['contest_id']
        self.room_group_name = f'standings_{self.contest_id}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        # await self.send_standings({'standings': ['Hello']})

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    
    async def send_standings(self, event):
        standings = event['standings']

        await self.send(text_data=json.dumps({
            'standings': standings
        }))
