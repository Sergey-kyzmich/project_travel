import eel
import database
from check_logical_error import check_logical_error, repl
eel.init("web")

database.create_db()

@eel.expose
def write_to_db(country, city, geogr_obg, date_start, date_end, comment, ocenca, active):
    country, city, geogr_obg, comment = repl(country, city, geogr_obg, comment)
    database.add(country, city, geogr_obg, date_start, date_end, comment, ocenca, active)

@eel.expose
def open_html_file(name_file_open):
    eel.show(name_file_open)


@eel.expose
def add_to_html_table():
    data=[]
    for id in range(1, database.len_db()+1):
        data.append(database.give_line(id))
    print(data, database.len_db())
    return {"len_table":database.len_db(), 
            "data":data}
@eel.expose
def check_error(country, city, geogr_obg, date_start, date_end, comment, ocenca, active):
    ch_l_e = check_logical_error(country, city, geogr_obg, date_start, date_end, comment, ocenca, active)
    ch_l_e.check_timedelta()
    ch_l_e.check_empty_input()
    ch_l_e.check_no_in_input()
    ch_l_e.check_num_in_input()
    ch_l_e.check_on_future()
    ch_l_e.add_n()
    return ch_l_e.error

database.create_db()
eel.start("main_index.html")