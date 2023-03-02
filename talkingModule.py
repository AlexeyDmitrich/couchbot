from pymystem3 import Mystem

# http://p-bot.ru/api/getAnswer

#users_input = input('введите тестовый текст \n')
analyse = Mystem()
def vocablary_text(users_input):
    text = ''.join(analyse.lemmatize(users_input)).rstrip('\n')
    return text

#text = vocablary_text(users_input)
#print(text)