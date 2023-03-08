import telebot
from telebot import types
import menu
import json
import functions as func
import requests
import languageModule
from languageModule import translator as tran
import talkingModule
import time
from logger import dump as log

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

user = 'anonymus*'
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

def error(message, info, description='Кажется, всё сломалось'):
    global user
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIHM2QEpe_v0Vn-YUI1w2QGZIFY6r_nAAJCBwACRvusBH1aiEB35lPMLgQ') #'CAACAgIAAxkBAAIDjmP8y9nCt64diU-3bguNT_3csgABlQACagEAAs6YzRYbIlPARgMMCC4E')
    bot.send_message(message.chat.id, description)
    try:
        log(user,message.text,description,"НЕЯВНОЕ ИСКЛЮЧЕНИЕ")
    except:
        print('Сбой логгирования при добавлении:')
        print(user,message.text,description,info)

@bot.message_handler(commands=['start'])
def start_message(message):
    global user
    global load_status
    try:
        bot.send_message(message.chat.id, "добро пожаловать!")
        user=message.from_user.id
        output = func.load(user)
        load_status = True
        print(f"user={message.from_user.id}")
    #    print(message)
        bot.send_message(message.chat.id, output)
        # telebot.types.InlineKeyboardButton('меню', callback_data='меню')
        # bot.send_message(message.chat_id, text='Меню')
    except:
        error(message, 'не удаётся загрузить сеанс', 'Ошибка в модуле start_message')

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
    bot.send_message(message.chat.id, text="*МЕНЮ*", reply_markup=choise, parse_mode='MARKDOWN')

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

#@bot.message_handler(func= lambda message:True, content_types=['text', 'sticker'])

    
@bot.message_handler(regexp='спасибо')
def thank_user(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIHQ2QErs4HgWCIDatcozgEDaavRlH4AAI2BwACRvusBAqX86rdUV82LgQ')
    bot.send_message(message.chat.id, "Вежливость по отношению к боту это так мило! 🥰 _Обращайтесь_)", parse_mode='MARKDOWN')
    log(user, message.text, "ответ на благодарность")

#@bot.message_handler(func= lambda message:True, content_types=['text', 'sticker'])


@bot.message_handler(content_types=['text'])
def data_input(message):
    global dialog
    global replic
    global vacancy
    global need_skill

    try:
        if dialog == 1:
            if languageModule.translator((message.text).lower()) != '/stop':
                for skill in ((message.text).lower()).split(';'):
                    func.base_of_skills.append(skill.strip())
                # func.base_of_skills.append(((message.text).lower()).split(';'))
                if (message.text).lower() == 'гениальность':
                    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIDfGP8x7p_xx1of1dE_Tft16jDoBI8AAJGIwACZ1aZSQfInwNd_rM3LgQ')
                    bot.send_message(message.chat.id, 'Простите. Продолжайте.')
                log(user, message.text, "добавляем в базу навыков")
            else:
                menu.working(message.from_user.id, '/stop')
                bot.send_message(message.chat.id, 'я постараюсь запомнить эти навыки')
                dialog = 0 
                log(user, message.text, "сохраняем")

        elif dialog == 2: 
            if languageModule.translator((message.text).lower()) != '/stop':
                vacancy = (message.text).lower()
                print(f'input vacancy: {vacancy}')
                dialog = 9
                replic = 'Введите требования к кандидату отдельными сообщениями, когда требования кончатся, отправьте "Стоп" \nВы можете вводить несколько требований в одном сообщении, разделяя их точкой с запятой (;)'
                log(user, message.text, "добавляем в базу вакансий")
                out_say(message, 3)            
            else: 
                bot.send_message(message.chat.id, 'записал')
                dialog = 0
                func.add_vacancy(vacancy, need_skill)
                log(user, message.text, "сохраняем")
                menu.working(message.from_user.id, '/stop')

        elif dialog == 3:
            if languageModule.translator((message.text).lower()) != '/stop':
                print(f'input text: {message.text}')
                for skill in ((message.text).lower()).split(';'):
                    func.base_of_vacancis.append(skill.strip())
                # need_skill.append((message.text).lower())
                dialog = 3
                log(user, message.text, "добавляем в требования к вакансии")
            else:
                dialog = 9
                replic = 'введите название следующей вакансии или скажите стоп, чтобы сохранить'
                out_say(message, 2)
                log(user, message.text, "закончили с этой вакансией")

        elif dialog == 4:
            check = func.check_vac(message.text)
            bot.send_message(message.chat.id, check)
            dialog = 0
            log(user, message.text, "формируем чек по вакансии")

        elif dialog == -1:
            if (languageModule.translator((message.text).lower()) != '/stop') and (languageModule.translator((message.text).lower()) != '/cancel'):
                func.delskill((message.text).lower())
                log(user, message.text, "удаляем навык из списка, не трогая .json")
            else:
                if languageModule.translator((message.text).lower()) == '/cancel':
                    bot.send_message(message.chat.id, 'Возвращаю всё как было')
                    dialog = 0
                    func.load(user)
                    log(user, message.text, "выполняем func.load(user)")
                else:
                    menu.working(message.from_user.id, '/stop')
                    bot.send_message(message.chat.id, 'Изменения сохранены')
                    dialog = 0
                    log(user, message.text, "выполняем /stop")
        
        elif dialog == -2:
            if (languageModule.translator((message.text).lower()) != '/stop') and (languageModule.translator((message.text).lower()) != '/cancel'):
                func.delvac((message.text).lower())
                log(user, message.text, "приступаем к удалению вакансии")
            else:
                if languageModule.translator((message.text).lower()) == '/cancel':
                    bot.send_message(message.chat.id, 'Возвращаю всё на место')
                    dialog = 0
                    func.load(user)
                    log(user, message.text, "выполняем func.load(user)")
                else:
                    menu.working(message.from_user.id, '/stop')
                    bot.send_message(message.chat.id, 'Изменения сохранены')
                    dialog = 0 
                    log(user, message.text, "выполняем /stop")

        else: 
            log(user, message.text, "выполняем understand к этому сообщению")
            understand(message)
        
    except:
        error(message, "Сбой при добавлении, удалении или чеке вакансии","Ошибка в диалоговом модуле при вводе данных")


def understand (message):
    global load_status
    global dialog
    global replic
    global menu_choise
    global user
    try:
        if load_status == False:
            user=message.from_user.id
            func.load(user)
            log(user, message.text, "func.load(user)")
            load_status = True
    except:
        error(message, "ошибка на входе в модуль understand", 'Не получается загрузить данные')
    
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
            print(user, message.text, translate)
            log(user, message.text, translate)
            output = str(menu.working(message.from_user.id, translate)) # команда уходит в меню
        
        
        if output != translate: # если команда что-то вернула, кроме самой себя
            print(output)
            bot.send_message(message.chat.id, output, parse_mode='MARKDOWN')       # (для команд, которые есть в меню)
            log(user, message.text, str(f"{translate} -> команда есть в меню, возвращаем значение "))
        else:   # если команды не нашлось

             # для добавления скиллов:
            if output == '/addskill':
                dialog = 9
                replic = 'Введите навык \nесли новых навыков больше нет, скажите стоп. \nВы можете вводить несколько навыков в одном сообщении, разделяя их точкой с запятой (;)'
                log(user, message.text, str(f"->{translate} : запрашиваем навык"))
                out_say(message, 1)
                    
            # для добавления вакансий
            elif output == '/addvac':
                dialog = 9
                replic = 'название вакансии: \n'
                log(user, message.text, str(f"->{translate} : запрашиваем название вакансии"))
                out_say(message, 2)

            elif output == '/demo':
                with open (f'vacancy.json', 'r', encoding='UTF-8') as vac:
                    func.base_of_vacancis = json.load(vac)
                dialog = 9
                replic = "Загружены демонстрационные вакансии"
                log(user, message.text, str(f"->{translate} : загружаем демо вакансии"))
                out_say(message, 0)
            
            elif output == '/checkvac':
                dialog = 9
                replic = 'Введите вакансию: \n'
                log(user, message.text, str(f"->{translate} : запрашиваем название вакансии"))
                out_say(message, 4)

            #для удаления навыков:
            elif output == '/delskill':
                dialog = 9
                replic = 'Отправьте названия навыков для их удаления, затем отправьте стоп - для сохранения изменений, или отмена - для сброса\n'
                log(user, message.text, str(f"->{translate} : запрашиваем название навыка"))
                out_say(message, -1)

            #для удаления вакансий:
            elif output == '/delvac':
                dialog = 9
                replic = 'Отправьте названия вакансий для их удаления, затем отправьте стоп - для сохранения изменений, или отмена - для сброса\n'
                log(user, message.text, str(f"->{translate} : запрашиваем название вакансии"))
                out_say(message, -2)


            elif output=='/hello': 
                if (load_status==False or(load_status==True and len(func.base_of_skills)<4)):
                    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIHB2QEjQIBEJD1pZvNYu8YY6WWN0ZHAAI-BwACRvusBK9cOl7BGYj2LgQ')
                    bot.send_message(message.chat.id, func.hello(), parse_mode='MARKDOWN')
                    log(user, message.text, "функция первого приветствия")
                else:
                    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIHB2QEjQIBEJD1pZvNYu8YY6WWN0ZHAAI-BwACRvusBK9cOl7BGYj2LgQ')
                    bot.send_message(message.chat.id, 'Здорово, что мы снова встретились!')
                    log(user, message.text, "функция обычного приветствия")

            elif output=='/bye':
                func.save(message.from_user.id)
                bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIHRmQEr-xvBpCV-JwHUCsDWaIaPrNeAAIuBwACRvusBPxoaF47DCKVLgQ')
                bot.send_message(message.chat.id, "До свидания! <b>Не забывайте добавлять навыки</b>.", parse_mode='HTML')
                log(user, message.text, "прощание")
              
            # AI для поддержания диалога
            else:
    #            bot.send_message(message.chat.id, output)
                try:
                    log(user, message.text, str(f"->{translate} : пробуем получить ответ у Павлова"))
                    talking(message)
                except:
                    log(user, message.text, str(f"->{translate} : Павлов ничего не вернул"))
                    bot.send_message(message.chat.id, str(f'Запрос: {output} \n не получилось обработать'))
    except:
        error(message, 'ошибка в основном блоке модуля understand', 'Что-то пошло не так. Попробуйте другой запрос.')


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
            error(message, "некорректный запрос", "API не может понять запрос")
            bot.send_message(message.chat.id, f'Запрос: "{qq}" не получилось обработать')
        print(res)
        bot.send_message(message.chat.id, res)
    except:
        error(message, 'Сторонее API не справилось с задачей', 'Так хотелось ответить Вам что-нибудь остроумное, но что-то сломалось')



def out_say(message, step=0):
    global dialog
    global replic
    try:
        if dialog == 9:
            bot.send_message(message.chat.id, replic)
            dialog = step
    except: 
        error(message, "Ошибка где-то в диалоге", 'Почему-то не получается построить диалог')
        

@bot.message_handler(content_types=['sticker'])
def sticker_input(message):
    try:
        print(message.sticker.file_id)
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIHNmQEpr_DbhX4NMDVVmtGL5rPbRrsAAJJBwACRvusBCGgUFw9zcWhLgQ') #'CAACAgIAAxkBAAIDj2P80Kf2YKS55GsH45nircucbFqjAAJBEQACA04JSn3DX5Qm6dIJLgQ')
        bot.send_message(message.chat.id, 'Что бы этот стикер значил? \n(пока это риторический вопрос)')
    except:
        error(message, "Исключение при обработке стикера")
        

        
bot.polling()