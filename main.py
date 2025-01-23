from bot import bot
from handlers.start_handlers import register_start_handlers
from handlers.game_handlers import register_game_handlers

register_start_handlers(bot)
register_game_handlers(bot)

bot.polling()