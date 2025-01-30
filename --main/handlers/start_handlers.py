from lexicon.lexicon import lexicon
from keyboards.keyboards import yes_no_kb

def register_start_handler(bot):
    @bot.message_handler(commands=["/start"])
    def start_handler(message):
     bot.send_message(chat_id=message.chat.id,
        text=lexicon.start,
        reply_markup=yes_no_kb
        )