import os
from telethon import TelegramClient
api_id = 24250238
api_hash = "cb3f118ce5553dc140127647edcf3720"
bot_token = "5900432090:AAGh66GjvNR0fnGCiOngV4rC5tg5pninmlU"
skeleton_url = ""

api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')
bot_token = os.environ.get('BOT_TOKEN')
skeleton_url = os.environ.get('SKELETON_URL')


bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)


