from django.urls import path
from .views import home, chat_bot

urlpatterns = [
    path('', home, name='home'),
    path('api/chat/', chat_bot, name='chat_bot'),
]
