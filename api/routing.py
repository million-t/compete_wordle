from django.urls import re_path
from api import consumers

websocket_urlpatterns = [
    re_path(r'ws/(?P<contest_id>\d+)/standings/$', consumers.StandingsConsumer.as_asgi()),
]