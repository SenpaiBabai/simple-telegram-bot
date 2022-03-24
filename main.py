from bot import Bot
from config import BOT_TOKEN

my_bot = Bot(token=BOT_TOKEN)

for event in my_bot.start_pooling():
    print(event.message.chat.username)