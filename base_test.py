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