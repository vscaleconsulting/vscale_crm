from telethon.sync import TelegramClient
from telethon.sessions import StringSession

client = TelegramClient(StringSession(), 1868530, "edf7d1e794e0b4a5596aa27c29d17eba")

client.connect()

print(client.session.save())
client.disconnect()