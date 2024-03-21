import random
from bot_settings import bot


def register_rndm_handlers():
    bot.register_message_handler(random_number, commands=['random'])


def random_number(message):
    rnd_number = random.randint(1, 10)
    bot.send_message(message.from_user.id, str(rnd_number))