import os
from telethon import TelegramClient
api_id = 23442389
api_hash = "70490ec8a810932cb5cb7f9d6a839ee0"
bot_token = "6107533276:AAHR4lKUnLGFvR6cpnUzjzvUCqNzLd69rZE"
skeleton_url = ""

api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')
bot_token = os.environ.get('BOT_TOKEN')
skeleton_url = os.environ.get('SKELETON_URL')


bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)


