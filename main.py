from aiogram.utils import executor
import create_bot

async def on_startup(_):
    print('Bot online')

import client

client.register_handlers_client(create_bot.dp)
client.register_handlers_other(create_bot.dp)

executor.start_polling(create_bot.dp, skip_updates=True, on_startup=on_startup)
