# Модуль для изучения новой технологии на предмет дальнейшего подключения к боту
import sqlite3 as sl

connect = sl.Connection('vacancy_skill.db')

# with connect:
#     connect.execute("""
#         CREATE TABLE VACANCY (
#             id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#             name TEXT,
#             need_skills TEXT
#         );
#     """)
    


sql = 'INSERT INTO VACANCY (name, need_skills) values(?, ?)'
data = []
n_skill = ''
vac_name = input("Введите название вакансии\n")
while n_skill != "Стоп":
    n_skill = input("добавьте требование\n")
    if n_skill != "Стоп":
        data.append((vac_name, n_skill))
    # id += 1

# print(data)
with connect:
    connect.executemany(sql, data)
        
        ###
# Этот блок кода пойдет в functions

# def check_skill_db (skill):
#     check = '''
#     '''
#     counter = 0
#     connect = sl.Connection('vacancy_skill.db')
#     with connect:
#         data = connect.execute("SELECT * FROM VACANCY WHERE need_skills == 'c#'")
#         for row in data:
#             counter +=1
#             check += "*\t"
#             check += (row[1])
#             check += "\n"
#         if counter > 0:
#             check += f"Навык будет полезен в {counter} специальностях"
#         else:
#             check += "Для выбранных специальностей этот навык, увы, бесполезен. Может работодатели его называют как-то иначе?"    
#     return check
        ###

