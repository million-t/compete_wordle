import json
from channels.generic.websocket import AsyncWebsocketConsumer
from compete_wordle.wsgi import *
from asgiref.sync import sync_to_async
from api.services.wordle_services import get_standings

class StandingsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.contest_id = self.scope['url_route']['kwargs']['contest_id']
        self.room_group_name = f'standings_{self.contest_id}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        
        standings = await sync_to_async(get_standings)(self.contest_id, 1, 50)
        await self.send(text_data=json.dumps({
            'standings': standings
        }))
        
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
