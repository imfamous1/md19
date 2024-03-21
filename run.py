from bot_settings import bot
from handlers import welcome, rndm


welcome.register_welcome_handlers()
rndm.register_rndm_handlers()

bot.polling(none_stop=True)
