# Модуль в разработке
import sqlite3 as sl

connect = sl.Connection('language.db')

# with connect:
#     connect.execute("""
#         CREATE TABLE HELLO (
#             id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#             phrase TEXT,
#             rate INTEGER
#         );
#      """)
#     connect.execute("""
#         CREATE TABLE BYE (
#             id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#             phrase TEXT,
#             rate INTEGER
#         );
#     """)
    

def add_phrase (table, phrase, rate=1):
    phrase = str(phrase).strip().lower()
    try:
        with connect:
            rate = connect.execute(f"SELECT * FROM {table} WHERE phrase LIKE '{phrase}'")
            for raw in rate:
                rate = raw[2]
                rate += 1
            print(rate)
            connect.execute(f"UPDATE {table} SET rate={rate} WHERE phrase LIKE '{phrase}'") 
    except:
        sql = f'INSERT INTO {table} (phrase, rate) values(?, ?)'
        data = (phrase, rate)
        with connect:
            connect.execute(sql, data)

phr = input('Фраза\n')
add_phrase('HELLO', phr)

with connect:
    db = connect.execute('SELECT * FROM HELLO')
    for raw in db:
        print(raw)