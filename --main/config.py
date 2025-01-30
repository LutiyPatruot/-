from environs import  Env

env = Env()
env.read_env() # читаем данные из .env
bot_token = env("BOT_TOKEN")