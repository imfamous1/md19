import sqlite3


connection = sqlite3.connect('base.db', check_same_thread=False)
cursor = connection.cursor()


def insert_user(user_id, name):
    with connection as conn:
        cursor = conn.cursor()
        cursor.execute('select user_id from subscriptions where user_id = ?', (user_id,))
        user = cursor.fetchone()
        if user is None:
            cursor.execute('insert into subscriptions (user_id, first_name) values (?, ?)', (user_id, name, ))
        else:
            pass


def insert_order_to_base(name, user_id, status, date):
    with connection as conn:
        cursor = conn.cursor()
        cursor.execute('insert into orders (model, user_id, date, status) values (?, ?, ?, ?)',
                       (name, user_id, status, date,))



def get_user_id_and_name():
    with connection as conn:
        result = conn.cursor().execute('select user_id, first_name from subscriptions').fetchall()
        return result


def get_products_by_category(category):
    with connection as conn:
        result = conn.cursor().execute('select name from products where category = ?',
                                       (category,)).fetchall()
        return result


def get_description_by_name(name):
    with connection as conn:
        result = conn.cursor().execute('select description, price, image from products where name = ?',
                                       (name,)).fetchone()
        return result


