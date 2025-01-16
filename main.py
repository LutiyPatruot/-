from bot import bot
from start_handler import register_start_handler

register_start_handler(bot)

bot.polling()