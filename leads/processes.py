from multiprocessing import Process
from threading import Thread
from pandas import read_csv
from telethon import events
from telethon import TelegramClient
from telethon.sessions import StringSession
from leads.models import TelegramMessage
from time import sleep
from threading import Thread
from asgiref.sync import sync_to_async, async_to_sync
import asyncio


def job(sess_str, ph_no):

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    client = TelegramClient(StringSession(sess_str),
                            1868530, "edf7d1e794e0b4a5596aa27c29d17eba", 
                            loop=loop)

    @sync_to_async
    def update_message(message):
        TelegramMessage.objects.create(
            message_id=message.id,
            sender_ph=ph_no,
            from_id=message.from_id.user_id,
            peer_id=message.peer_id.user_id,
            datetime=message.date,
            message=message.message,
            out=message.out
        )

    @client.on(events.NewMessage())
    async def handler(event):
        message = event.message
        print(message)
        await update_message(message)

    with client:
        client.run_until_disconnected()


sessions = read_csv('leads/sessions.csv')

threads = []

for _, session in sessions.iterrows():
    session_str = session['sess_str1']
    number = session['number']
    threads.append(Thread(target=job, args=(session_str, number)))

for thread in threads:
    thread.start()

print("threads spawned")

for thread in threads:
    thread.join()
