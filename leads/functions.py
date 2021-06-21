from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import asyncio


def get_user_id(username):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    sess_str = '1ApWapzMBu4bPq_KDVCy4vb0Y0V9IOjCcK3dQkKmIp3CL3adfUpeKznS5mzyYsM8rmwvlrWKAY8XwH1N3WqrHYfMNpXxaKuh-km9NUCwCpU9DeAbr07B3HfkypPzC7RM_mJIQzLB0h4CngnCwNJEFXva-AUlXPhcI2QLWgEaBVfce-Uys9UZ9ETL1QoMbZrkZzHKDa_aB3s2McSkkc9H4wTJHzfHpQYyH79AWABpCGNBtbb3sgrb9Qg5X29pdS41m5XhQWnEllJomISAPs88r2HsWFo_RtBq6_sEbrZ6fqDleE5BIKAaepYPCAY_t1ZFC5qlMXil8x_R6G0rf7aCYL0mrO6stmAQ='

    client = TelegramClient(StringSession(sess_str),
                            1868530, "edf7d1e794e0b4a5596aa27c29d17eba", loop=loop)

    client.connect()
    try:
        entity = client.get_entity('@' + username)
    except ValueError:
        client.disconnect()
        return -1
    except Exception:
        client.disconnect()
        return -2
    client.disconnect()
    return entity.id


def send_message(sender, receiver, message):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    sess_str = '1ApWapzMBu4bPq_KDVCy4vb0Y0V9IOjCcK3dQkKmIp3CL3adfUpeKznS5mzyYsM8rmwvlrWKAY8XwH1N3WqrHYfMNpXxaKuh-km9NUCwCpU9DeAbr07B3HfkypPzC7RM_mJIQzLB0h4CngnCwNJEFXva-AUlXPhcI2QLWgEaBVfce-Uys9UZ9ETL1QoMbZrkZzHKDa_aB3s2McSkkc9H4wTJHzfHpQYyH79AWABpCGNBtbb3sgrb9Qg5X29pdS41m5XhQWnEllJomISAPs88r2HsWFo_RtBq6_sEbrZ6fqDleE5BIKAaepYPCAY_t1ZFC5qlMXil8x_R6G0rf7aCYL0mrO6stmAQ='

    client = TelegramClient(StringSession(sess_str),
                            1868530, "edf7d1e794e0b4a5596aa27c29d17eba", loop=loop)

    client.connect()
    try:
        client.send_message(receiver, message)
        client.disconnect()
        return True
    except Exception:
        client.disconnect()
        return False
