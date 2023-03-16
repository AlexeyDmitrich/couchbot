# Модуль для изучения новой технологии на предмет дальнейшего подключения к боту
import sqlite3 as sl

connect = sl.Connection('vacancy_skill.db')

# with connect:
#     connect.execute("""
#         CREATE TABLE VACANCY (
#             id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#             name TEXT,
#             need_skills TEXT
#         );
#     """)
    


sql = 'INSERT INTO VACANCY (name, need_skills) values(?, ?)'
data = []
n_skill = ''
vac_name = input("Введите название вакансии\n")
while n_skill != "Стоп":
    n_skill = input("добавьте требование\n")
    if n_skill != "Стоп":
        data.append((vac_name, n_skill))
    # id += 1

# print(data)
with connect:
    connect.executemany(sql, data)


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