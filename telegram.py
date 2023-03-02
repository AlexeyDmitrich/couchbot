import telebot
import menu
import json
import functions as func
import requests
import languageModule
import talkingModule

try:
    with open ('token.json', 'r', encoding='UTF-8') as tk:
        API_TOKEN = (json.load(tk))
except:
    print('Не найден токен')
    new_token = input("Введите новый API-токен")
    try:
        with open ('token.json', 'w', encoding='UTF-8') as tk:
            tk.write(json.dumps(new_token, ensure_ascii=False))
    except:
        print("Не удалось привязать новый токен")
bot = telebot.TeleBot(API_TOKEN)
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
    except:
        error(message)

@bot.message_handler(content_types=['text'])
def data_input(message):
    global dialog
    global replic
    global vacancy
#    print (f'stable vacancy: {vacancy}')
    global need_skill
#    print (f'need_skill: {need_skill}')
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
                replic = 'Введите требования к кандидату отдельными сообщениями'
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

        else: understand(message)
    except:
        error(message)
        
def understand (message):
    global load_status
    global dialog
    global replic
    try:
        if load_status == False:
            user=message.from_user.id
            func.load(user)
            load_status = True
    except:
        error(message, 'Не получается загрузить данные')
    try:    
        text = message.text
        print(text)
        output = 'ожидаю ввода:'
        translate = ''
        
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
            
            #для удаления навыков:
#            elif output == '/delskill':
                

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