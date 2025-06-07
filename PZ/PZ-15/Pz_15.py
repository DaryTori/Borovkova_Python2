#Приложение КАФЕДРА для автоматизации работы отдела кадров ВУЗа. Таблица
#Преподавательский состав должна содержать следующие данные: Табельный номер,
#Фамилия И.О., Дата рождения, Должность, Ученая степень, Нагрузка, Зарплата.

import sqlite3 as sq

with sq.connect('kafedra.db') as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS teachers")
    cur.execute("""CREATE TABLE IF NOT EXISTS teachers(
                number INTEGER PRIMARY KEY AUTOINCREMENT,
                fio TEXT NOT NULL,
                birth_date DATE NOT NULL,
                post TEXT NOT NULL,
                academ_degree TEXT NOT NULL,
                workload TEXT NOT NULL,
                salary REAL NOT NULL
                )""")

from info import info_teachers

cur.executemany("INSERT INTO teachers VALUES (?, ?, ?, ?, ?, ?, ?)", info_teachers)

cur.execute("SELECT * FROM teachers WHERE salary >= 50000 and academ_degree='Доктор наук'")
print('Вывод один: ')
for result in cur:
    print(result)
cur.execute("SELECT number, fio, post FROM teachers WHERE academ_degree='Кандидат наук' ORDER BY salary ASC")
print('Вывод два: ')
for result in cur:
    print(result)
cur.execute("SELECT number, fio, post, workload, salary FROM teachers WHERE post='Преподаватель философии' or post='Преподаватель биологии' ORDER BY number DESC")
print('Вывод три: ')
for result in cur:
    print(result)

cur.execute("DELETE FROM teachers WHERE number=5")
cur.execute("DELETE FROM teachers WHERE salary>70000 and workload != '48 часов в неделю'")
cur.execute("DELETE FROM teachers WHERE birth_date='2000-09-15'")

cur.execute("UPDATE teachers SET workload='35 часов в неделю' WHERE salary=50000")
cur.execute("UPDATE teachers SET academ_degree='Кандидат наук' WHERE number=3")
cur.execute("UPDATE teachers SET post='Преподаватель обществознания' WHERE birth_date='1999-01-30'")

cur.execute("SElECT * FROM teachers")
print('Итоговый вывод: ')
for result in cur:
    print(result)