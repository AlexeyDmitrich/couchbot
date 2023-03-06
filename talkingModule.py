from pymystem3 import Mystem

#users_input = input('введите тестовый текст \n')
analyse = Mystem()

def vocablary_text(users_input):
    punctuation = """'~!@#$%^&*()_+=-`:"?><,./|}]{["№;:?"""
    text = str(users_input)
    for sym in text:
        if sym in punctuation:
            text = text.replace(sym, '')
    text = ''.join(analyse.lemmatize(text)).rstrip('\n')
    return text

#text = vocablary_text(users_input)
#print(text)