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


def insert_order_to_base(model, user_id, date, payment, status, order_id):
    with connection as conn:
        cursor = conn.cursor()
        cursor.execute('insert into orders (model, user_id, date, payment, status, order_id) values (?, ?, ?, ?, ?, ?)',
                       (model, user_id, date, payment, status, order_id))


def insert_order_to_orders_cache(id, user_id, status):
    with connection as conn:
        cursor = conn.cursor()
        cursor.execute('insert into orders_cache (id, user_id, last_known_status) values (?, ?, ?)',
                       (id, user_id, status, ))


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


def get_order_details(user_id):
    with connection as conn:
        result = conn.cursor().execute('select id, model, date, payment, status from orders where user_id = ?',
                                       (user_id,)).fetchall()
        return result


def get_current_status_by_order_id(order_id):
    with connection as conn:
        result = conn.cursor().execute('select status, user_id from orders where order_id = ?',
                                       (order_id,)).fetchone()
        return result


def get_last_known_status_by_order_id(id):
    with connection as conn:
        result = conn.cursor().execute('select last_known_status from orders_cache where id = ?',
                                       (id,)).fetchone()[0]
        return result


def update_last_known_status(status, id):
    with connection as conn:
        conn.cursor().execute('update orders_cache set last_known_status = ? where id = ?', (status, id, ))
