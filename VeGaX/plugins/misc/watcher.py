from pyrogram import filters
from pyrogram.types import Message

from VeGaX import app
from VeGaX.core.call import Ayush

welcome = 20
close = 30


@app.on_message(filters.video_chat_started, group=welcome)
@app.on_message(filters.video_chat_ended, group=close)
async def welcome(_, message: Message):
    await Ayush.stop_stream_force(message.chat.id)
