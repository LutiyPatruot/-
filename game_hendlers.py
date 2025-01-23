from lexicon.lexicon import lexicon

def register_game_handlers(bot):
    @bot.message_handlers(func=lambda message: message.text == lexicon.yes_button)
    def yes_register_game_handlers(message):
            bot.send_message(
                chat_id=message.chat.id,
                text=lexicon.yes,
                reply_markup=None
            )