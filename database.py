# create_db() - создает таблицу, если еще не создана

# add(...) - добавляет в таблицу данные country (str), city (str), geogr_obj (str), date_start (str/date), date_end (str/date), comment (str), ocenca (int), active (int))
# Пример: add("country", "city", "geogr_obg", "14-07-2007", "14-07-2024", "comment", 1, 2)

# edit(...) - изменяет строку в таблице (id (int),country (str), city (str), geogr_obj (str), date_start (str/date), date_end (str/date), comment (str), ocenca (int), active (int))
# Если какое-либо значение изменять не требуется, то на его месте передать ""
# Пример: edit(1, "country", "city", "nngeogr_obg", "14-07-2007", "14-07-2024", "", 1, 2)

# delete_db() - удаляет таблицу(полностью)

# delete_from_db(int) - удаляет строку из таблицы (принимает id строки)

# give_line(int) - возвращает данные о строке (принимает id строки)

# len_db() - возвращает длину таблицы 

# give_column(str) - возвращает данные о столбце(принимает название столбца)
# название всех столбцов и их типы: id (INTEGER PRIMARY KEY), country (STRING), city (STRING), geogr_obg (STRING), date_start (DATE), date_end (DATE), comment (STRING), ocenca (INTEGER), active (INTEGER)

import sqlite3
import eel


@eel.expose
def add(country, city, geogr_obg, date_start, date_end, comment, ocenca, active):
    db = sqlite3.connect('db_travel.db')
    cursor = db.cursor()
    id = len(list(cursor.execute("SELECT id from travel")))+1
    cursor.execute((f'INSERT INTO travel  VALUES ("{id}", "{country}", "{city}", "{geogr_obg}", "{date_start}", "{date_end}", "{comment}", "{ocenca}", "{active}")'))
    db.commit()
    db.close()

@eel.expose
def create_db():
    db = sqlite3.connect('db_travel.db')
    cursor = db.cursor()
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS travel (
    id INTEGER PRIMARY KEY,
    country STRING,
    city STRING,
    geogr_obg STRING,
    date_start DATE,
    date_end DATE,
    comment STRING,
    ocenca INTEGER,
    active INTEGER
    )
    ''')
    db.commit()
    db.close()


@eel.expose
def delete_all_db():
    db = sqlite3.connect('db_travel.db')
    cursor = db.cursor()
    cursor.execute("""DROP TABLE travel""")
    db.commit()
    db.close()


@eel.expose
def delete(id):
    db = sqlite3.connect('db_travel.db')
    cursor = db.cursor()
    cursor.execute(f'DELETE FROM travel WHERE id = {id}')
    db.commit()
    db.close()


@eel.expose
def edit(id, country, city, geogr_obg, date_start, date_end, comment, ocenca, active):
    db = sqlite3.connect('db_travel.db')
    cursor = db.cursor()
    print(id, country, city, geogr_obg, date_start, date_end, comment, ocenca, active)
    if country!="":cursor.execute(f'''UPDATE travel SET country = "{country}" WHERE id = {id}''');db.commit()
    if city!="":cursor.execute(f'''UPDATE travel SET city = "{city}" WHERE id = {id}''');db.commit()
    if geogr_obg!="":cursor.execute(f'''UPDATE travel SET geogr_obg = "{geogr_obg}" WHERE id = {id}''');db.commit()
    if date_start!="":cursor.execute(f'''UPDATE travel SET date_start = "{date_start}" WHERE id = {id}''');db.commit()
    if date_end!="":cursor.execute(f'''UPDATE travel SET date_end = "{date_end}" WHERE id = {id}''');db.commit()
    if comment!="":cursor.execute(f'''UPDATE travel SET comment = "{comment}" WHERE id = {id}''');db.commit()
    if ocenca!="":cursor.execute(f'''UPDATE travel SET ocenca = "{ocenca}" WHERE id = {id}''');db.commit()
    if active!="":cursor.execute(f'''UPDATE travel SET active = "{active}" WHERE id = {id}''');db.commit()
    db.close()


@eel.expose
def give_line(id):
    db = sqlite3.connect('db_travel.db')
    cursor = db.cursor()
    res = cursor.execute(f"SELECT * FROM travel WHERE id = {id}")
    for i in res:
        db.close()
        return i


@eel.expose
def give_column(name):
    db = sqlite3.connect('db_travel.db')
    cursor = db.cursor()
    res = cursor.execute(f"SELECT {name} FROM travel")
    a = []
    for i in res:
        a.append(i[0])
    db.close()
    return a

@eel.expose
def len_db():
    db = sqlite3.connect('db_travel.db')
    cursor = db.cursor()
    a = len(list(cursor.execute("SELECT id from travel")))
    db.close()
    return a