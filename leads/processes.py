from multiprocessing import Process
from pandas import read_csv
from telethon import events
from telethon import TelegramClient
from telethon.sessions import StringSession
from leads.models import TelegramMessage
from time import sleep
from threading import Thread
from asgiref.sync import sync_to_async, async_to_sync



def job(sess_str, ph_no):
    client = TelegramClient(StringSession(sess_str),
                            1868530, "edf7d1e794e0b4a5596aa27c29d17eba")
    # client.connect()
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
        print('hello')
        message = event.message
        await update_message(message)

    with client:
        # while True:
        #     sleep(10000000)
        client.run_until_disconnected()


sessions = read_csv('leads/sessions.csv')

processes = []

for _, session in sessions.iterrows():
    session_str = session['sess_str1']
    number = session['number']
    processes.append(Process(target=job, args=(session_str,number)))

for process in processes:
    process.start()

for process in processes:
    process.join()
