def translator (users_text):
    start = '/startrungoстартпускпоехалиначалиничинайначнемначнём'
    stop = '/stopстопостановитьхватитпрекратиуйтивыходвыйтизакончитьдостаточносохранитьвсёexitquit'
    help = '''/helpmanualпомощьпомочьпомогитемануалсправка'''
    show = 'showviewopenпокажипоказатьпросмотретьпосмотретьвзглянутьоткрытьоткройвсесформируйвыведивывести'
    add = 'добавитьдобавьвнестивнесидополнитьсоздатьсоздай'
    addvac = '/addvacвакансиивакансиювакант' 
    addskill = '/addskillопытумениеуменияпрактикускиллынавыки'  
    rate = '/ratestatisticрейтингстатистикастатистикупроанализируй' 
    delete = '/deleteудалитьснесиснестиуничтожьуничтожитьаннигилироватьаннигилируйубериубрать'
    demo = '/demoдемонстрацияпробныетестовыепримерные'
    
    
    if str(users_text).split()[0].lower() in add:
        if str(users_text).split()[-1].lower() in addvac:
            return '/addvac'
        elif str(users_text).split()[-1].lower() in addskill:
#            print(str(users_text).split()[-1])
            return '/addskill'
        else:
            return users_text

    elif str(users_text).split()[0].lower() in show:
        if str(users_text).split()[-1].lower() in addvac:
            return '/allvac'
        elif str(users_text).split()[-1].lower() in addskill:
#            print(f"{((str(users_text).split()[-1]).upper)}:")
            return '/allskill'
        elif str(users_text).split()[-1].lower() in rate:
#            print(f"{(str(users_text).split()[-1].upper)}:")
            return '/rate'
        else:
            return users_text
    
    elif str(users_text).split()[0].lower() in delete:
        if str(users_text).split()[-1].lower() in addvac:
            return '/delvac'
        elif str(users_text).split()[-1].lower() in addskill:
#            print(f"{((str(users_text).split()[-1]).upper)}:")
            return '/delskill'
        else:
            return users_text
    elif str(users_text).split()[-1].lower() in demo:
        return '/demo'
            
    else:
        for i in range(len(list((users_text).split()))):
            # print(str(users_text).split()[i].lower())
            if str(users_text).split()[i].lower() in stop:
                return '/stop'
            else:
                for i in range(len(list((users_text).split()))):
                    # print(str(users_text).split()[i].lower())
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


    