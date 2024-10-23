from django.urls import re_path
from api import consumers

websocket_urlpatterns = [
    re_path(r'ws/standings/(?P<contest_id>\d+)/$', consumers.StandingsConsumer.as_asgi()),
]