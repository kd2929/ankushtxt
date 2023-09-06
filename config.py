import os
from telethon import TelegramClient
api_id = 21080577
api_hash = "23bf3f7e84830378c419effeef1624e3"
bot_token = "6469469309:AAGdLA-o5h975CGAG8giGtCPfnzrq1HpsO8"
skeleton_url = ""

api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')
bot_token = os.environ.get('BOT_TOKEN')
skeleton_url = os.environ.get('SKELETON_URL')


bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)


