import random
from bot_settings import bot
import sqlite as db
import time


def register_rndm_handlers():
    bot.register_message_handler(send_user_orders, regexp='Заказы')


def send_user_orders(message):

    details = db.get_order_details(message.from_user.id)
    text = ""
    for id, model, date, payment, status in details:
        text += f"Номер заказа: {id}.\nМодель: {model}\nДата заказа: {date}\nСтатус оплаты: {payment}\nСтатус заказа: *{status}*\n\n"

    bot.send_message(message.from_user.id, text, parse_mode='markdown')


def auto_order_status_check():
    while True:  # бесконечный цикл
        current_status, user_id = db.get_current_status_by_order_id(1)
        last_known_status = db.get_last_known_status_by_order_id(1)
        if last_known_status != current_status:
            bot.send_message(user_id, f"Ваш статус заказа изменился: {current_status}")
            db.update_last_known_status(current_status, 1)

        time.sleep(5)

    # schedule - модули для расписания, например напоминаний
    # введение
    # 1 анализ предметной области
    # 1.1 - структура бота
    # 2 анализ информационных технологий
    # 3 разработка бота
    # заключение
