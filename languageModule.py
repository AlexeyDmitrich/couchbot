def translator (users_text):
    start = '/startrungoстартпускпоехалиначалиничинайначнемначнёмпривет)))привет!'
    stop = '/stopстопостановитьхватитпрекратиуйтивыходвыйтизакончитьдостаточносохранитьвсёвсеexitquit'
    help = '''/helpmanualпомощьпомочьпомогитемануалсправка'''
    show = 'showviewopenпокажипоказатьпросмотретьпосмотретьвзглянутьоткрытьоткройсформируйвыведивывести'
    add = 'добавитьдобавьвнестивнесидополнитьсоздатьсоздай'
    addvac = '/addvacвакансиивакансиювакант' 
    addskill = '/addskillопытумениеуменияпрактикускиллынавыки'  
    rate = '/ratestatisticрейтингстатистикастатистикупроанализируй' 
    delete = '/deleteудалитьснесиснестиуничтожьуничтожитьаннигилироватьаннигилируйубериубрать'
    demo = '/demoдемонстрацияпробныетестовыепримерные'
    cancel = '/cancelresetотменитьотменазабейотставить'
    check = '/checkupчекнипроверьсовместимость'
    find = '/findjobработуподходящуюнайдипоищиработаподойдетосилю'
    
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


    