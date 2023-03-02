import languageModule as lm
import functions as func
#import telegram as tg

def working (user, choise=''):
#    while True:
    #        choise = input("\n Введите команду \n (ну или попросите помочь) \n")
    #choise = lm.translator(choise) # TODO: translator
    match (choise):
        case '/start':
            return func.load(user)
        case '/stop':
#           if request.lower() in yes:
            return func.save(user)
#            print('Не забывайте добавлять новые навыки! \n До новых встреч!')
#                break
        case '/help':
            return func.print_help()
#        case '/addvac':
#            return func.add_vacancy()
#        case '/addskill':
#            return func.add_skill()
        case '/allvac':
            return func.allpreview(func.base_of_vacancis)
        case '/allskill':
            return func.allpreview(func.base_of_skills)
        case '/rate':
            return func.rate()
        case _:
            return choise
