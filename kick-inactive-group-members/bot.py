from config import Config
from pyrogram import Client

plugins = dict(root="plugins")
app = Client(
     'inkick-bot',
      bot_token = 1513564664:AAHXjEh-Em7natUk7si8-wQdodrVG5rBWP0,
      api_id = 2504577,
      api_hash = fd1c39658dc2736f41b006ad55b0dcae,
      plugins = plugins
)
app.run()
