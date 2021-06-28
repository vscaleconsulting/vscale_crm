from telethon import TelegramClient, events
from telethon.sessions import StringSession

# sess_str = '1BJWap1sBu1YkgNU7CN1YXFyfJCScUtsHjaMTgePxjSU3tS0LJrLGFIK5e14lwhYKjX39G_K1c9M7RYxP22wsuyTv6-dzSC813TlQ2Ducc4GD_ULuVrjN8Zi-bbpZiOoClBDjCJ9iMWkEEkBpOWFbJXHK1Ja24I1SV0wjoih4hACMq8RWEsgmnfcORsL7iNuVccQUEA6nCX-r77qZGDLVl6Z8NchXFpG-I0xiwstakysKnTtsygccA4qEheqSJPfSnIv8b2XZtyKca21Hbb_okOvK-OgUQFapyGGBheZoSlz-I1dhsaMNnDrVV18R7ecX2M8NBrkvb1fQ7FFgNPEevWfKDR84r98='

client = TelegramClient(StringSession(), 1868530, "edf7d1e794e0b4a5596aa27c29d17eba", sequential_updates=True)

user = '@vaishavdhepe'

# @client.on(events.NewMessage(chats=user))
# async def handler(event):
#     print(event.message.message)

async def main():
    print(client.session.save())
    # @client.on(events.NewMessage(chats=user, incoming=True))
    # async def handler(event):
    #     print(event.message.message)

    # async with client:
    #     while True:
    #         message = await aioconsole.ainput('<<< ')
    #         if message == "":
    #             continue
    #         if message == 'disconnect':
    #             await client.disconnect()
    #         await client.send_message(user, message)


with client:
    client.loop.run_until_complete(main())
    # client.run_until_disconnected()