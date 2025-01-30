from telebot import TeleBot, types
from lexicon.lexicon import lexicon

bytton_yes = types.KeyboardButton(text=lexicon.no_button)
bytton_no = types.KeyboardButton(text=lexicon.yes_button)
yes_no_kb = types.ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
)
yes_no_kb.add(bytton_yes, bytton_no)

bytton_rock = types.KeyboardButton(text=lexicon.rock)
bytton_paper = types.KeyboardButton(text=lexicon.paper)
bytton_scissors = types.KeyboardButton(text=lexicon.scissors)
game_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
game_kb.add(bytton_rock)
game_kb.add(bytton_paper)
game_kb.add(bytton_scissors)