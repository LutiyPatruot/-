from bot import bot
from handlers.start_handlers import register_start_handler
from handlers.game_handlers import register_game_handlers

register_start_handler(bot)
register_game_handlers(bot)
print(1)
bot.polling()