import json as js
import sqlite3 as sl

stdin = input('ожидаю ввода: \n')

# arr = []

# arr.append((stdin.lower()).strip().split(';'))

# print(f'stdin \t:\t {stdin}\nstdout \t:\t {arr}')

print(stdin.removeprefix("/"))

# try:
#     with open (f'vacancy.json', 'r', encoding='UTF-8') as vac:
#         base_of_vacancis = js.load(vac)
#         load_text_vac = ('база вакансий загружена\n')
# except:
#     print('Excception')
    
# for vac in base_of_vacancis:
#     print (vac[0])
#     for skill in vac[1]:
#         print (skill)
        
# connect = sl.Connection('vacancy_skill.db')
# with connect:
#     data = connect.execute("SELECT * FROM VACANCY WHERE need_skills == 'c#'")
#     for row in data:
#         print(row[1])