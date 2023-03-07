import talkingModule as tm

test_text = input('ожидается ввод тестовой фразы:\n')

def translator (users_text):
    users_text = tm.vocablary_text(users_text)

    hello = ['привет','добрый день','приветствовать','здравствовать','приветик','добрый время сутки','добрый вечер','добрый утро']
    start = ['/start', 'run', 'go', 'старт', 'пуск', 'поехать', 'начинать'] 
        #   '/start run go старт пуск поехали начали начинай начнем начнём'
    stop = ['/stop', 'стоп', 'останавливать', 'хватить', 'прекращать', 'уходить', 'выход', 'выходить', 'заканчивать', 'достаточно', 'сохранять', 'все', 'exit', 'quit']
        #  '/stop стоп остановить хватит прекрати уйти выход выйти закончить достаточно сохранить всё все exit quit'
    help = ['/help','manual','помощь','помогать','мануал','справка'] 
        #  '/help manual помощь помочь помогите мануал справка мочь уметь'
    show = ['show','view','open','показывать','просматривать','посмотреть','глянуть','взглядывать','открывать','сформировывать','вывести'] 
        #  'show view open покажи показать просмотреть посмотреть взглянуть открыть открой сформируй выведи вывести'
    add = ['добавлять','вносить','дополнять','создавать' ]
        # 'добавить добавь внести внеси дополнить создать создай'
    addvac = ['/addvac','вакансия','вакант'] 
        #    '/addvac вакансии вакансию вакант' 
    addskill = ['/addskill','опыт','умение','практика','скилла','скил','навык']
        #      '/addskill опыт умение умения практику скиллы скилл скилы скил навыки'  
    rate = ['/rate','statistic','рейтинг','статистика','проанализировать'] 
        #  '/rate statistic рейтинг статистика статистику проанализируй' 
    delete = ['/delete','удалять','снести','уничтожать','аннигилироваться','убирать'] 
        #    '/delete удалить снеси снести уничтожь уничтожить аннигилировать аннигилируй убери убрать'
    demo = ['/demo','демонстрация','пробный','тестовый','примерный'] 
        #  '/demo демонстрация пробные тестовые примерные'
    cancel = ['/cancel','reset','отменять','отмена','забивать','отставлять'] 
        #    '/cancel reset отменить отмена забей отставить'
    check = ['/checkup','чекать','чек','проверять','совместимость'] 
        #   '/checkup чекни чек проверь совместимость'
    find = ['/findjob','работа','подходить','находить','поискать','осиливать'] 
        #  '/findjob работу подходящую найди поищи работа подойдет осилю'

    def construct_phrase (users_text):
        potential_command = ''
        for word in users_text.split():
            if word in start:
                potential_command += "start"
            if word in stop:
                potential_command += "stop"
            if word in hello:
                potential_command += "hello"
            # if word in bye:
            #     potential_command += "bye"

            if word in help:
                potential_command += "help"
            if word in show:
                potential_command += "show"
            if word in add:
                potential_command += "add"
            if word in find:
                potential_command += "find"  
            if word in delete:
                potential_command += "delete"  
            if word in check:
                potential_command += "check"

            if word in addvac:
                potential_command += "vacancy"
            if word in demo:
                potential_command += "demo"
            if word in addskill:
                potential_command += "skill"
            if word in rate:
                potential_command += "rate"

            if word in cancel:
                potential_command += "cancel"
        

        return potential_command
    
    return construct_phrase(users_text)

                                                          

    for word in str(users_text).lower().split():
        if word in start:
            return '/start'
        elif word in find:
            return '/find'

    if str(users_text).split()[0].lower() in add:
        if str(users_text).split()[-1].lower() in addvac:
            return '/addvac'
        elif str(users_text).split()[-1].lower() in addskill:
            return '/addskill'
        else:
            return users_text

    elif str(users_text).split()[0].lower() in show:
        if str(users_text).split()[-1].lower() in addvac:
            return '/allvac'
        elif str(users_text).split()[-1].lower() in addskill:
            return '/allskill'
        elif str(users_text).split()[-1].lower() in rate:
            return '/rate'
        elif str(users_text).split()[-1].lower() in check:
            return '/check'
        else:
            return users_text
    
    elif str(users_text).split()[0].lower() in delete:
        if str(users_text).split()[-1].lower() in addvac:
            return '/delvac'
        elif str(users_text).split()[-1].lower() in addskill:
            return '/delskill'
        else:
            return users_text
    elif str(users_text).split()[-1].lower() in demo:
        return '/demo'
            
    else:
        for i in range(len(list((users_text).split()))):
            if str(users_text).split()[i].lower() in cancel:
                return '/cancel'
            elif str(users_text).split()[i].lower() in stop:
                return '/stop'
            else:
                for i in range(len(list((users_text).split()))):
                    if str(users_text).split()[i].lower() in help:
                        return '/help'
                    else:
                        if str(users_text).lower() in addvac:
                            return '/addvac'
                        elif str(users_text).lower() in addskill:
                            return '/addskill'
                        elif str(users_text).lower() in rate:
                            return '/rate'
                        else:
                            return users_text




print(translator(test_text))