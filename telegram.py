import telebot
from telebot import types
import menu
import json
import functions as func
import requests
import languageModule
import talkingModule
import time


try:
    with open ('token.json', 'r', encoding='UTF-8') as tk:
        API_TOKEN = (json.load(tk))
except:
    print('Не найден токен')
    new_token = input("Введите новый API-токен:\n")
    try:
        with open ('token.json', 'w', encoding='UTF-8') as tk:
            tk.write(json.dumps(new_token, ensure_ascii=False))
        time.sleep(3)
        with open ('token.json', 'r', encoding='UTF-8') as tk:
            API_TOKEN = (json.load(tk))
    except:
        print("Не удалось привязать новый токен")
try:
    bot = telebot.TeleBot(API_TOKEN)
    print('Бот настроен')
except:
    print('Запуск бота не удался. Попробуйте перезапустить программу.')

API_URL = 'https://7012.deeppavlov.ai/model'

users = [] # нужен какой-то учёт пользователей
user = ''
load_status = False
dialog = 0 
# 0 - стоп
# 1 - ожидание ввода навыка
# 2 - ожидание ввода вакансии
# 3 - ожидание ввода требования
# 9 - исходящие
menu_choise = ''
replic = 'пустой респонз'
vacancy = ''
need_skill = []

def error(message, description='Кажется, всё сломалось'):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIDjmP8y9nCt64diU-3bguNT_3csgABlQACagEAAs6YzRYbIlPARgMMCC4E')
    bot.send_message(message.chat.id, description)

@bot.message_handler(commands=['start'])
def start_message(message):
    global user
    global users
    global load_status
    try:
        bot.send_message(message.chat.id, "добро пожаловать!")
        users.append(message.from_user.id)
        user=message.from_user.id
        output = func.load(user)
        load_status = True
        print(f"user={message.from_user.id}")
    #    print(message)
        bot.send_message(message.chat.id, output)
        # telebot.types.InlineKeyboardButton('меню', callback_data='меню')
        # bot.send_message(message.chat_id, text='Меню')
    except:
        error(message)

@bot.message_handler(commands=['menu'])#, regexp='меню')
def gui_menu(message):
    choise = telebot.types.InlineKeyboardMarkup()
    choise.add(telebot.types.InlineKeyboardButton(text='Загрузить тестовые вакансии', callback_data='/demo'))     
    choise.add(telebot.types.InlineKeyboardButton(text='Добавить вакансии в базу', callback_data='/addvac'))
    choise.add(telebot.types.InlineKeyboardButton(text='Добавить навыки в резюме', callback_data='/addskill'))
    choise.add(telebot.types.InlineKeyboardButton(text='Посмотреть на вакансии', callback_data='/allvac'))
    choise.add(telebot.types.InlineKeyboardButton(text='Инфо о вакансии', callback_data='/check'))
    choise.add(telebot.types.InlineKeyboardButton(text='Полюбоваться навыками', callback_data='/allskill'))
    choise.add(telebot.types.InlineKeyboardButton(text='Общая статистика', callback_data='/rate'))
    choise.add(telebot.types.InlineKeyboardButton(text='Подбор подходящих вакансий', callback_data='/find'))
    choise.add(telebot.types.InlineKeyboardButton(text='Как пользоваться ботом?', callback_data='/help'))
    bot.send_message(message.chat.id, text="МЕНЮ", reply_markup=choise)

@bot.message_handler(regexp='меню')
def gui_menu_from_text(message):
    choise = telebot.types.InlineKeyboardMarkup()
    choise.add(telebot.types.InlineKeyboardButton(text='Загрузить тестовые вакансии', callback_data='/demo'))     
    choise.add(telebot.types.InlineKeyboardButton(text='Добавить вакансии в базу', callback_data='/addvac'))
    choise.add(telebot.types.InlineKeyboardButton(text='Добавить навыки в резюме', callback_data='/addskill'))
    choise.add(telebot.types.InlineKeyboardButton(text='Посмотреть на вакансии', callback_data='/allvac'))
    choise.add(telebot.types.InlineKeyboardButton(text='Инфо о вакансии', callback_data='/check'))
    choise.add(telebot.types.InlineKeyboardButton(text='Полюбоваться навыками', callback_data='/allskill'))
    choise.add(telebot.types.InlineKeyboardButton(text='Общая статистика', callback_data='/rate'))
    choise.add(telebot.types.InlineKeyboardButton(text='Подбор подходящих вакансий', callback_data='/find'))
    choise.add(telebot.types.InlineKeyboardButton(text='Как пользоваться ботом?', callback_data='/help'))
    bot.send_message(message.chat.id, text="МЕНЮ", reply_markup=choise)

@bot.callback_query_handler(func=lambda call: True) 
def query_handler(call):
    global menu_choise
    global dialog
    global replic
    message = call.message
    bot.answer_callback_query(callback_query_id=call.id, text='Сейчас попробуем')
    answer = ''
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    if call.data == '/demo':
        answer = ('/demo')
        with open (f'vacancy.json', 'r', encoding='UTF-8') as vac:
            func.base_of_vacancis = json.load(vac)
        dialog = 9
        replic = "Загружены демонстрационные вакансии"
        out_say(message, 0)
    elif call.data == '/addvac':
        answer = ('/addvac')
        dialog = 9
        replic = 'Введите название вакансии: \n'
        out_say(message, 2)
    elif call.data == '/addskill':
        dialog = 9
        replic = 'Введите навык \nесли новых навыков больше нет, скажите стоп \n'
        out_say(message, 1)
    elif call.data == '/check':
        dialog = 9
        replic = 'Введите вакансию: \n'
        out_say(message, 4)
    elif call.data == '/allvac':
        bot.send_message(message.chat.id, menu.working(call.from_user.id, '/allvac'))
    elif call.data == '/allskill':
        bot.send_message(message.chat.id, menu.working(call.from_user.id, '/allskill'))
    elif call.data == '/rate':
        bot.send_message(message.chat.id, menu.working(call.from_user.id, '/rate'))
    elif call.data == '/find':
        bot.send_message(message.chat.id, menu.working(call.from_user.id, '/find'))
    elif call.data == '/help':
        bot.send_message(message.chat.id, menu.working(call.from_user.id, '/help'))
    # bot.send_message(call.message.chat.id, answer) 
    # menu_choise = answer
    # dialog = 5




@bot.message_handler(content_types=['text'])
def data_input(message):
    global dialog
    global replic
    global vacancy
    global need_skill

    try:
        if dialog == 1:
            if languageModule.translator((message.text).lower()) != '/stop':
                func.base_of_skills.append((message.text).lower())
                if (message.text).lower() == 'гениальность':
                    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIDfGP8x7p_xx1of1dE_Tft16jDoBI8AAJGIwACZ1aZSQfInwNd_rM3LgQ')
                    bot.send_message(message.chat.id, 'Простите. Продолжайте.')
            else:
                menu.working(message.from_user.id, '/stop')
                bot.send_message(message.chat.id, 'я постараюсь запомнить эти навыки')
                dialog = 0 

        elif dialog == 2: 
            if languageModule.translator((message.text).lower()) != '/stop':
                vacancy = (message.text).lower()
                print(f'input vacancy: {vacancy}')
                dialog = 9
                replic = 'Введите требования к кандидату отдельными сообщениями, когда требования кончатся, отправьте "Стоп"'
                out_say(message, 3)            
            else: 
                bot.send_message(message.chat.id, 'записал')
                dialog = 0
                func.add_vacancy(vacancy, need_skill)
                menu.working(message.from_user.id, '/stop')

        elif dialog == 3:
            if languageModule.translator((message.text).lower()) != '/stop':
                print(f'input text: {message.text}')
                need_skill.append((message.text).lower())
                dialog = 3
            else:
                dialog = 9
                replic = 'введите название следующей вакансии или скажите стоп, чтобы сохранить'
                out_say(message, 2)

        elif dialog == 4:
            check = func.check_vac(message.text)
            bot.send_message(message.chat.id, check)
            dialog == 0

        elif dialog == -1:
            if (languageModule.translator((message.text).lower()) != '/stop') and (languageModule.translator((message.text).lower()) != '/cancel'):
                func.delskill((message.text).lower())
            else:
                if languageModule.translator((message.text).lower()) == '/cancel':
                    bot.send_message(message.chat.id, 'Возвращаю всё как было')
                    dialog = 0
                    func.load(user)
                else:
                    menu.working(message.from_user.id, '/stop')
                    bot.send_message(message.chat.id, 'Изменения сохранены')
                    dialog = 0
        
        elif dialog == -2:
            if (languageModule.translator((message.text).lower()) != '/stop') and (languageModule.translator((message.text).lower()) != '/cancel'):
                func.delvac((message.text).lower())
            else:
                if languageModule.translator((message.text).lower()) == '/cancel':
                    bot.send_message(message.chat.id, 'Возвращаю всё на место')
                    dialog = 0
                    func.load(user)
                else:
                    menu.working(message.from_user.id, '/stop')
                    bot.send_message(message.chat.id, 'Изменения сохранены')
                    dialog = 0 

        else: understand(message)
    except:
        error(message)
        
def understand (message):
    global load_status
    global dialog
    global replic
    global menu_choise
    try:
        if load_status == False:
            user=message.from_user.id
            func.load(user)
            load_status = True
    except:
        error(message, 'Не получается загрузить данные')
    
    text = message.text
    print(text)
    
    
    output = '/menu'
    translate = ''

    try:                
        
        if dialog == 5:
            text = menu_choise
            dialog = 0
        
        if dialog == 0:

            translate = languageModule.translator(text)     # переводим речь в команду для бота
            # если подходящей команды не нашлось - возвращаем фразу в неизменном виде    
            output = str(menu.working(message.from_user.id, translate)) # команда уходит в меню
        
        
        if output != translate: # если команда что-то вернула, кроме самой себя
            print(output)
            bot.send_message(message.chat.id, output)       # (для команд, которые есть в меню)
        else:   # если команды не нашлось

             # для добавления скиллов:
            if output == '/addskill':
                dialog = 9
                replic = 'Введите навык \nесли новых навыков больше нет, скажите стоп \n'
                out_say(message, 1)
                    
            # для добавления вакансий
            elif output == '/addvac':
                dialog = 9
                replic = 'название вакансии: \n'
                out_say(message, 2)

            elif output == '/demo':
                with open (f'vacancy.json', 'r', encoding='UTF-8') as vac:
                    func.base_of_vacancis = json.load(vac)
                dialog = 9
                replic = "Загружены демонстрационные вакансии"
                out_say(message, 0)
            
            elif output == '/check':
                dialog = 9
                replic = 'Введите вакансию: \n'
                out_say(message, 4)

            #для удаления навыков:
            elif output == '/delskill':
                dialog = 9
                replic = 'Отправьте названия навыков для их удаления, затем отправьте стоп - для сохранения изменений, или отмена - для сброса\n'
                out_say(message, -1)

            #для удаления вакансий:
            elif output == '/delvac':
                dialog = 9
                replic = 'Отправьте названия вакансий для их удаления, затем отправьте стоп - для сохранения изменений, или отмена - для сброса\n'
                out_say(message, -2)
              
            # AI для поддержания диалога
            else:
    #            bot.send_message(message.chat.id, output)
                try:
                    talking(message)
                except:
                    bot.send_message(message.chat.id, f'Запрос: {output} \n не получилось обработать')
    except:
        error(message, 'Что-то пошло не так. Попробуйте другой запрос.')


def talking(message):
    try:
        quest = talkingModule.vocablary_text(str(message.text))
        print(quest)
        qq = ""
        for word in quest:
            qq = str(qq + word)
        print (qq)
    #    qq = " ".join(quest)
        data = {"question_raw":[qq]}
        print(f'запрос: {data}')
        try:
            res = requests.post(API_URL, json=data, verify=False).json()
        except:
            bot.send_message(message.chat.id, f'Запрос: "{qq}" не получилось обработать')
        print(res)
        bot.send_message(message.chat.id, res)
    except:
        error(message, 'Так хотел ответить Вам что-нибудь остроумное, что случайно всё сломал')



def out_say(message, step=0):
    global dialog
    global replic
    try:
        if dialog == 9:
            bot.send_message(message.chat.id, replic)
            dialog = step
    except: 
        error(message, 'Почему-то не получается построить диалог')
        

@bot.message_handler(content_types=['sticker'])
def sticker_input(message):
    try:
        print(message.sticker.file_id)
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIDj2P80Kf2YKS55GsH45nircucbFqjAAJBEQACA04JSn3DX5Qm6dIJLgQ')
        bot.send_message(message.chat.id, 'Что бы этот стикер значил? \n(пока это риторический вопрос)')
    except:
        error(message)
        

        
bot.polling()