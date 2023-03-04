import json as js


base_of_skills = ["нажимание кнопок", "смотрение в монитор", "стремление к развитию"] # список коротких строк
base_of_vacancis = [["Deep Learning Специалист", ["ml", "искусственный интеллект", "speech synthesis", "deep learning", "machine learning", "artificial intelligence", "машинное обучение", "voice to lip synch", "ai"], 0]]  # список списков/словарь (или т.п.). Уместить: должность - скиллы - уровень соответствия
# модель вакансии: [название, [навык-1, навык-2, ..., навык-n], рейтинг] рейтинг - техническая переменная, которая расчитывается

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
        Он предназначен для помощи в подборе работы, исходя из имеющихся навыков,
        или для определения недостающих навыков для желаемых вакансий.
        Бот расчитан на работу с простыми запросами на русском языке, например:
                \tдобавить вакансию
                \tстатистика
                \tстарт
                \tстоп
                \tпомоги
                \tи т.д.
        Если вдруг он не понял команду - в разделе помощи можно найти команды, которые он точно знает.
        А ещё можно попытаться переформулировать запрос (это бесплатно).
        При внесении данных о вакансиях и навыках, бот формирует базу, с помощью которой
        будет подсказывать Вашу совместимость с какой-либо вакансией. При выходе из бота, он предложит
        сохранить сеанс. Если это сделать - то при следующем запуске вакансии и навыки останутся в базе.
               
        Сохранённый сеанс пока отсутствует. Это ничего, сейчас создадим.
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

def print_help ():
    man_text = ('''
    Бот расчитан на взаимодействие с простыми командами на русском языке,
    сформулированными одним - двумя словами без знаков препинания.
    Но этот метод ещё в разработке, поэтому, вот перечень основных команд,
    если он не понял по-русски:
    /start \t- начать взаимодействие с ботом
    /addvac \t- добавить вакансию с требованиями в список вакансий
    /addskill \t- добавить свой новый опыт (духовный не учитывается)
    /allvac \t- просмотр имеющихся вакансий
    /allskill \t- просмотр своего опыта
    /rate \t- посмотреть совместимость своего опыта с имеющимися вакансиями
    /stop \t- остановить бота (будет предложено сохранить сеанс)
    /help \t- показать эту страницу помощи
    ''')
    return man_text

def menu ():
    menu_text = ('''
    
    ''')

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
    for vac in base_of_vacancis:
        if vac[0] == vacancy:
            check+= (f'Вакансия: {(vac[0])}\nИмеющиеся навыки:\n')
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
            check += (f'\n Вы на {percent}% подготовлены к этой работе')
            
    return check

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
    top = 2
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
        check += ('Имеющиеся навыки:\n')
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
        check += (f'Вы на {percent}% подготовлены к этой работе\n---------------\n')
        return check
    
    propose += (f" На данном этапе Вам больше всего стоит присмотреться к следующим вакансиям:")
    propose += (f" \n{form_check(lead1)} ")
    propose += (f" \n{form_check(lead2)} ")
    propose += (f" \n{form_check(lead3)} ")
    
    return propose