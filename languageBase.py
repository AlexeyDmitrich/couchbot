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


        # Этот блок кода пойдет в тело бота
                    ###

# if dialog == 8:
#     @bot.message_handler(content_types=['text'])
#     def gui_menu(message):
#         choise = telebot.types.InlineKeyboardMarkup()
#         choise.add(telebot.types.InlineKeyboardButton(text='Приветствие', callback_data='hello')) 
#         choise.add(telebot.types.InlineKeyboardButton(text='Прощание', callback_data='bye')) 
#         choise.add(telebot.types.InlineKeyboardButton(text='Запрос к функционалу', callback_data='menu'))
#         choise.add(telebot.types.InlineKeyboardButton(text='Светская беседа', callback_data='talk'))   
#         choise.add(telebot.types.InlineKeyboardButton(text='Не запоминать это', callback_data='cancel')) 
#         bot.send_message(message.chat.id, text="Что бы это значило?", reply_markup=choise)

#     @bot.callback_query_handler(func=lambda call: True) 
#     def query_handler_talk(call):
#         global menu_choise
#         global dialog
#         global replic
#         message = call.message
#         bot.answer_callback_query(callback_query_id=call.id, text='Я запомню это')
#         answer = ''
#         bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
#         if call.data == 'hello':
#             answer = ('hello')
# ## TODO: реализовать добавление в БД

#         elif call.data == 'bye':
#             answer = ('hello')
# ## TODO: реализовать добавление в БД

#         elif call.data == 'menu':
#             answer = ('menu')
# ## TODO: реализовать добавление в БД
#             return gui_menu_from_text
        
#         elif call.data == 'cancel':
#             bot.send_message(message.chat.id, text="Ок, я это забуду")

#         elif call.data == 'talk':
#             bot.send_message(message.chat.id, text="А можно подробнее?")
#             return talk_menu
            
#         def talk_menu(message):
#             choise = telebot.types.InlineKeyboardMarkup()
#             choise.add(telebot.types.InlineKeyboardButton(text='Это вопрос', callback_data='qu')) 
#             choise.add(telebot.types.InlineKeyboardButton(text='Это ответ на вопрос', callback_data='an')) 
#             choise.add(telebot.types.InlineKeyboardButton(text='Это предложение', callback_data='todo'))
#             choise.add(telebot.types.InlineKeyboardButton(text='Это юмор', callback_data='talk'))   
#             # choise.add(telebot.types.InlineKeyboardButton(text='', callback_data='cancel')) 
#             bot.send_message(message.chat.id, text="Что бы это значило?", reply_markup=choise)


                    ###