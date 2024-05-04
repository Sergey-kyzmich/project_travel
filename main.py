import eel
import database
eel.init("web")

database.create_db()

@eel.expose
def write_to_db(country, city, geogr_obg, date_start, date_end, comment, ocenca, active):
    database.add(country, city, geogr_obg, date_start, date_end, comment, ocenca, active)

@eel.expose
def open_html_file(name_file):
    eel.show(name_file)
        

@eel.expose
def add_to_html_table():
    data=[]
    for id in range(1, database.len_db()+1):
        data.append(database.give_line(id))
    print(data, database.len_db())
    return {"len_table":database.len_db(), 
            "data":data}

database.create_db()
eel.start("main_index.html")