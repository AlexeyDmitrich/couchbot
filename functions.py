import json as js


base_of_skills = ["нажимание кнопок", "смотрение в монитор", "стремление к развитию"] # список коротких строк
base_of_vacancis = [["Deep Learning Специалист", ["ml", "искусственный интеллект", "speech synthesis", "deep learning", "machine learning", "artificial intelligence", "машинное обучение", "voice to lip synch", "ai"], 0]]  # список списков/словарь (или т.п.). Уместить: должность - скиллы - уровень соответствия
# модель вакансии: [название, [навык-1, навык-2, ..., навык-n], рейтинг] рейтинг техническая переменная, которая расчитывается
# при добавлении вакансии. В случае, если у кандидата есть нужные навыки - бот сообщит ему об этом.
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
        # load_text_add_skills = ('Давайте для начала выясним, что Вы уже умеете?')
        # add_skill()
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
    сформулированными одним словом.
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
    test_text = "Мы Вам поможем. Потом."
    return man_text
    
def add_skill ():
    global base_of_skills
    print('''
    Этот раздел нужен для добавления своего опыта/навыков/знаний/умений, 
    что там ещё у Вас есть. Очень рекомендую для каждого навыка вызывать 
    эту команду отдельно. Позвольте дать Вам ещё совет: вводите название 
    навыка так, как его указывает работодатель в описании вакансии.
    ''')
    skill = ' '
    while skill != '':
        skill = input('Введите навык и нажмите enter, \nесли новых навыков больше нет, просто нажмите enter \n')
        if skill != '':
            base_of_skills.append(skill.lower())
            print ('Навык добавлен \n')

def add_vacancy (name, skills):
    global base_of_vacancis
    # print ('''
    # Здесь всё не так просто, как с добавлением навыков, но, если выполнять все подсказки
    # бота - то добавить новую вакансию не составит труда. 
    # ''')
    name = name  # input('Для начала введите название вакансии: \n')
    print(name)
    skills = skills
    print(skills)
    # skill = ' '
    rate = 0
    # while skill != '':
    #     skill = input('''
    #     Введите одно из требований к кандидату и нажмите Enter. 
    #     Этот вопрос будет задан снова, если требований больше нет,
    #     просто нажмите Enter \n''')
    #     if skill != '':
    #         skills.append(skill.lower())
    for skill in skills:
        if skill in base_of_skills:
            rate += 1
    if rate >= len(skills):
        print('Есть вероятность, что Вы идеально подходите этой работе. Или она Вам.\n')
    elif rate > len(skills)/2:
        print('Вы более, чем наполовину обладаете нужными качествами для этой вакансии.\n')
    elif rate > 0:
        print('Кое-что из того, чего хочет работодатель Вы умеете.\n')
    base_of_vacancis.append([name, skills, rate])
    print('Вакансия добавлена! \n')

def delskill(skill):
    global base_of_skills
    base_of_skills.remove(skill)
    
def delvac(vac):
    global base_of_vacancis
    for vacancy in base_of_vacancis:
        if vacancy[0] == vac:
            base_of_vacancis.remove(vacancy)
            

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
    #print (rate_to_vacancy)
    res = ''
    for key, value in rate_to_vacancy.items():
        for i in range(len(value)):
            # print(value[i][0])
            # print(key)
            res += (f"Вакансия: {value[i][0]} \t\t Рейтинг: {key}/{len(value[i][1])} \n")
    return(f'{rate_head} \n{res}')
    
    # for key in rate_to_vacancy:
    #     print(f"Вакансия: {rate_to_vacancy[key]} \t Рейтинг: {key}/{len(rate_to_vacancy[key][1])} ")
