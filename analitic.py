import database
import eel
#count_country() подсчёт государств
#count_native_country() подсчёт отечественных государств
#count_city() функция подсчёта городов
#count_geoobj() функция подсчёта посещенных мест
#ocenca_otech_and_zar() функция подсчета оценки зарубежных и отечественных курортов
@eel.expose
def count_country():#подсчёт государств
    count_gos=0#подсчет государств
    countries=[]#массив со всеми странами
    column_country=database.give_column("country")#массив со всеми странами
    for i in column_country:
        i=i.lower()
        if i in countries:
            count_gos+=0
        else:
            count_gos+=1
            countries.append(i)
    return count_gos


@eel.expose
def count_native_country():#подсчёт отечественных государств
    count_otec=0#подсчет отечественных государств
    countries=[]#массив со всеми странами
    column_country=database.give_column("country")#колонка из введеного
    for name_country in column_country:
        name_country=name_country.lower()
        if check_otech_country(name_country):
                if name_country not in countries:
                     count_otec+=1
                     countries.append(name_country)
    return count_otec

@eel.expose
def count_city():#функция подсчёта городов
    count_town=0#подсчет городов
    cities=[]#массив со всеми городами(без повторов)
    column_city=database.give_column("city")#массив со всеми городами
    for i in column_city:
        i=i.lower()
        if i not in cities:
            count_town+=1
            cities.append(i)
    return count_town

@eel.expose
def count_geoobj():#функция подсчёта посещенных мест
    count_places=0#подсчет посещенных мест
    places=[]#массив со всеми посещенными местами(без повторов)
    column_geoobj=database.give_column("geogr_obg")#массив со всеми посещенными местами
    for i in column_geoobj:
        i=i.lower()
        if i not in places:
            count_places+=1
            places.append(i)
    return count_places


def check_otech_country(name_country):
    if sum(["рф" in name_country,"россия" in name_country,"беларусь" in name_country,"казахстан" in name_country,
"таджикистан"in name_country, "российская федерация" in name_country, "узбекистан" in name_country, "киргизстан" in name_country, 
"узбекистан" in name_country, "кндр" in name_country, "корейская народная демократическая республика" in name_country])>=1:
        return True
    else:
        return False


@eel.expose    
def ocenca_otech_and_zar():
    column_country=database.give_column("country")
    ocenca = database.give_column("ocenca")
    otech_ocenca, otech_count, zar_ocenca, zar_count = 0,0,0,0
    for i in range(len(column_country)):
        if column_country[i]!="":
            if check_otech_country(column_country[i]):
                otech_ocenca += ocenca[i]
                otech_count += 1
            else:
                zar_ocenca+=ocenca[i]
                zar_count+=1
    if otech_count==0: sr_otech = None
    else: sr_otech = round(otech_ocenca/otech_count, 2)

    if zar_count==0: sr_zar = None
    else: sr_zar = round(zar_ocenca/zar_count, 2)

    return sr_otech, sr_zar

def ocenca_active_and_nactive():
    active = database.give_column("active")
    ocenca = database.give_column("ocenca")
    count_active, count_nactive, ocenca_active, ocenca_nactive = 0,0,0,0
    for i in range(len(ocenca)):
        if ocenca<3:
            count_nactive +=1
            ocenca_nactive +=ocenca[i]
        else:
            count_active +=1
            ocenca_active+=ocenca[i]
    if ocenca_active==0:sr_active = None
    else:sr_active = round(ocenca_active/count_active, 2)

    if ocenca_nactive==0: sr_nactive = None
    else:sr_nactive = round(ocenca_nactive/count_nactive, 2)

    return sr_active, sr_nactive 