from bot_settings import bot
from handlers import welcome, rndm
import threading

welcome.register_welcome_handlers()
rndm.register_rndm_handlers()

thread1 = threading.Thread(target=rndm.auto_order_status_check)
thread1.start()


bot.polling(none_stop=True)
