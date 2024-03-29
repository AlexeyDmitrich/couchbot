import json as js
import sqlite3 as sl

base_of_skills = ["нажимание кнопок", "смотрение в монитор", "стремление к развитию"] # список коротких строк
base_of_vacancis = [["Deep Learning Специалист", ["ml", "искусственный интеллект", "speech synthesis", "deep learning", "machine learning", "artificial intelligence", "машинное обучение", "voice to lip synch", "ai"], 0]]  # список списков/словарь (или т.п.). Уместить: должность - скиллы - уровень соответствия
# модель вакансии: [название, [навык-1, навык-2, ..., навык-n], рейтинг] рейтинг - техническая переменная, которая расчитывается
# for skill in base_of_skills:
#     skill = skill.strip()


rate_to_vacancy = {}

def load (user):
    global base_of_skills
    global base_of_vacancis
    try:
        with open (f'{user}skills.json', 'r', encoding='UTF-8') as sk:
            base_of_skills = js.load(sk)
            load_text_sk = ('база навыков загружена')
        with open (f'{user}vacancy.json', 'r', encoding='UTF-8') as vac:
            base_of_vacancis = js.load(vac)
            load_text_vac = ('база вакансий загружена\n')
        return(f'\n{load_text_sk}\n{load_text_vac}\n')
    except:
        load_text_first = ('''
               Привет! 
        Похоже, что Вы впервые пользуетесь этим ботом.
        Он предназначен для помощи в построении образовательной траектории для выхода на желаемую должность, 
        так же Вы сможете видеть, в каких вакансиях могут пригодиться Ваши навыки. 
        Бот расчитан на работу с простыми запросами на русском языке, например:
            \t- добавить вакансию
            \t- статистика
            \t- старт
            \t- стоп
            \t- помоги
            \t- и т.д.
        Если вдруг он не понял команду - в разделе помощи можно найти команды, которые он точно знает.
        А ещё можно попытаться переформулировать запрос (это бесплатно).
        При внесении данных о вакансиях и навыках, бот формирует базу, с помощью которой
        будет подсказывать Вашу совместимость с какой-либо вакансией. При выходе из бота, он предложит
        сохранить сеанс. Если это сделать - то при следующем запуске вакансии и навыки останутся в базе.
               
        Сохранённый сеанс пока отсутствует. Это ничего, сейчас создадим. 
        
        Для начала взаимодействия просто отправьте "Привет".
               ''')
        save(user)
        load_text_ready = ('Готово! Ботом можно пользоваться.')
        return(f'{load_text_first}\n\n {load_text_ready}')

def save (user):
    global base_of_skills
    global base_of_vacancis
    try:
        with open (f'{user}skills.json', 'w', encoding='UTF-8') as sk:
            sk.write (js.dumps (base_of_skills, ensure_ascii=False))
            save_text_sk = ("База навыков успешно сохранена")
    except:
        save_text_sk = ("Не удалось сохранить новые навыки")
    try:
        with open (f'{user}vacancy.json', 'w', encoding='UTF-8') as vac:
            vac.write (js.dumps (base_of_vacancis, ensure_ascii=False))
            save_text_vac = ("База вакансий успешно сохранена")
    except:
        save_text_vac = ("Не удалось сохранить новые вакансии")
    return(f'{save_text_sk}\n{save_text_vac}')

def hello():
    hello_message = ('''
    *Привет!* 
    Я - бот, который поможет прокачать навыки для устройства на работу. 
    Я стараюсь понимать простые запросы на русском языке, но это не всегда получается, так что рядом с окном ввода есть кнопка *меню*.
    
    Прежде всего нужно нажать кнопку *Загрузить сеанс* - так я пойму с кем общаюсь и смогу загрузить нужные данные.
    
    Далее Вам нужно будет добавлять свои навыки и желаемые вакансии. Но обо всём по порядку.
    
    В меню есть кнокпа - _Загрузить тестовые вакансии_, если её нажать - в Вашей подборке вакансий появятся несколько популярных вакансий для IT специалистов.
    
    Для добавления вакансий, которые интересны именно Вам, в меню тоже есть специальная кнопка. 
    А ещё Вы можете просто написать мне: *Добавь вакансии*, и мы обсудим вакансии и требования к ним.
    
    Ещё очень важно добавлять в своё "резюме" навыки. Записывать их надо в той же форме, как Вы записали их в вакансии. 
    Если будет отличаться регистр (размер букв) - я пойму, а вот с дополнительными символами и пробелами у меня проблемы(((
    Кстати, хочу Вас попросить избегать знаков препинания в нашем разговоре. Думаю, это временная проблема.
    
    В любой момент Вы можете посмотреть статистику и узнать на сколько Вы готовы к той или иной работе. А когда решите - мы сможем заняться подбором подходящих вакансий. 
    Для этого просто скажите мне: "*Найди работу*", 
    и я покажу три самых подходящих вакансии.
    ''')
    return hello_message

def print_help ():
    man_text = ('''
    Бот расчитан на взаимодействие с простыми командами на русском языке.
    Но этот метод ещё в разработке, поэтому, вот перечень основных команд,
    если он не понял по-русски:
    /start \t- начать взаимодействие с ботом
    /hello \t- инициализация сеанса
    /addvac \t- добавить вакансию с требованиями в список вакансий
    /addskill \t- добавить свой новый опыт (духовный не учитывается)
    /demo \t- загрузить пробные вакансии
    /allvac \t- просмотр имеющихся вакансий
    /allskill \t- просмотр своего опыта
    /rate \t- посмотреть совместимость своего опыта с имеющимися вакансиями
    /find \t- подобрать работу по навыкам
    /dellvac \t- удалить вакансию
    /dellskill \t- удалить навык
    /stop \t- сохранить сеанс
    /bye \t- сохранить и завершить сеанс
    /help \t- показать эту страницу помощи
    ''')
    return man_text

def add_vacancy (name, skills):
    global base_of_vacancis
    name = name  # input('Для начала введите название вакансии: \n')
    skills = skills
    rate = 0
    base_of_vacancis.append([name, skills, rate])


# метод для удаления навыков:
# принимает название навыка
# удаляет навык из документа base_of_skills    
def delskill(skill):
    global base_of_skills
    base_of_skills.remove(skill)
    
# метод для удаления вакансий:
# принимает название вакансии
# ищет в списке вакансий те, нулевые значения которых соответствуют названию в запросе
# удаляет вакансию из документа base_of_vacancis  
def delvac(vac):
    global base_of_vacancis
    for vacancy in base_of_vacancis:
        if vacancy[0] == vac:
            base_of_vacancis.remove(vacancy)

# просмотр всех вакансий
def allpreview (base):
    global base_of_vacancis
    res = ''
    if base == base_of_vacancis:
        for item in base: 
            res += str(item[0])
            res += '\n'
    else:
        for item in base: 
            res += str(item)
            res += '\n'
    return res
    
# просмотр статистики    
def rate ():
    global base_of_vacancis
    global rate_to_vacancy
    global base_of_skills
    
    rate_to_vacancy.clear()
    for vacancy in base_of_vacancis:
        rate = 0
        key = rate
        rate_to_vacancy.setdefault(key,[])
        for skill in vacancy[1]:
            if skill in base_of_skills:
                rate += 1
        key = rate
        rate_to_vacancy.setdefault(key,[])
        rate_to_vacancy [rate].append(vacancy)

    rate_head = ('Рейтинг компетенций пересчитан.\n')
    res = ''
    for key, value in rate_to_vacancy.items():
        for i in range(len(value)):
            res += (f"Вакансия: {value[i][0]} \t\t Рейтинг: {key}/{len(value[i][1])} \n")
    return(f'{rate_head} \n{res}')

# чек вакансии
def check_vac (vacancy):
    check = '''
    '''
    counter = 0
    for vac in base_of_vacancis:
        if vac[0].lower() == vacancy.lower():
            counter += 1
            check+= (f'\n********\nВакансия: {(vac[0])}\nИмеющиеся навыки:\n')
            count_of_skills = len(vac[1])
            rate_counter = 0
            for skill in vac[1]:
                if skill in base_of_skills:
                    check += (f' + {skill}\n')
                    rate_counter += 1
            if rate_counter == 0: check += (" -- нет --\n")
            check+= (f'Недостающие навыки:\n')
            for skill in vac[1]:
                if skill not in base_of_skills:
                    check += (f' - {skill}\n')
            percent = (rate_counter/count_of_skills)*100
            check += (f'\n Вы на {round(percent, 1)}% подготовлены к этой работе\n')
    if counter == 0:
        check = ('Вакансия с таким названием не найдена. \n Скажите "покажи вакансии", и я пришлю все, какие есть')
    return check

# чек навыка
def check_skill (skill):
    global base_of_vacancis
    check = '''
    '''
    counter = 0
    vacs = '' 
    for vac in base_of_vacancis:
        if str(skill).lower().rstrip() in vac[1]:
            counter += 1
            vac_skills_to_str = ''
            for value in vac[1]:
                vac_skills_to_str += f"{value}, "
            vac_skills_to_str = vac_skills_to_str.removesuffix(', ')
            vac_to_str = f'**{vac[0]}** ({vac_skills_to_str})\n'
            vacs += f'\n \t☑️ {vac_to_str}'
    if counter > 0:
        check += f'Навык будет полезен для: \n{vacs}'
        if ((counter+10)%10==1) and (counter!=11):
            check += f"\n Навык пригодится в {counter} специальности."
        else:
            check += f"\n Навык пригодится в {counter} специальностях."
        percent = round((counter/len(base_of_vacancis))*100)
        check += f"\nВ специалистах с этим навыком заинтересованы {percent}% работодателей."
    else:
        check += "Для выбранных специальностей этот навык, увы, бесполезен. Может работодатели его называют как-то иначе?"    
    return check


# подбор подходящих вакансий
def find_me_job ():
    global base_of_skills
    global base_of_vacancis
    propose = '''
    '''
    for vac in base_of_vacancis:
        count_of_skills = len(vac[1])
        rate_counter = 0
        for skill in vac[1]:
            if skill in base_of_skills:
                rate_counter += 1
        percent = (rate_counter/count_of_skills)*100
        vac[2] = percent
  
    lead1 = base_of_vacancis[0]
    lead2 = base_of_vacancis[0]
    lead3 = base_of_vacancis[0]
    top = 3
    while top !=0:
        for vac in base_of_vacancis:
            if vac[2] >= lead1[2]:
                lead1 = vac
            elif vac[2] >= lead2[2]:
                lead2 = vac
            elif vac[2] >= lead3[2]:
                lead3 = vac
        top -= 1
        
    def form_check (vac):
        global base_of_vacancis
        global base_of_skills
        check = '''
        '''
        check += (f'{vac[0]}')
        count_of_skills = len(vac[1])
        rate_counter = 0
        check += ('\nИмеющиеся навыки:\n')
        for skill in vac[1]:
            if skill in base_of_skills:
                check += (f' + {skill}\n')
                rate_counter += 1
        if rate_counter == 0: check += (" -- нет --\n")
        check+= (f'Недостающие навыки:\n')
        for skill in vac[1]:
            if skill not in base_of_skills:
                check += (f' - {skill}\n')
        percent = (rate_counter/count_of_skills)*100
        check += (f'Вы на {round(percent, 1)}% подготовлены к этой работе\n---------------\n')
        return check
    
    propose += (f" На данном этапе Вам больше всего стоит присмотреться к следующим вакансиям:")
    propose += (f" \n{form_check(lead1)} ")
    propose += (f" \n{form_check(lead2)} ")
    propose += (f" \n{form_check(lead3)} ")
    
    return propose