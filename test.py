import database
def count_country():#подсчёт государств
    count_gos=0#подсчет государств
    countries=[]#массив со всеми странами
    column_country=database.give_column("country")#массив со всеми странами
    print(column_country)
    for i in column_country:
        i=i.lower()
        if i in countries:
            count_gos+=0
        else:
            count_gos+=1
            countries.append(i)
    return count_gos



def count_native_country():#подсчёт отечественных государств
    count_otec=0#подсчет отечественных государств
    countries=[]#массив со всеми странами
    column_country=database.give_column("country")#колонка из введеного
    for name_country in column_country:
        name_country=name_country.lower()
        if sum(["рф" in name_country,
                "россия" in name_country,
                "беларусь" in name_country,
                "казахстан" in name_country,
                "киргизстан"in name_country,
                "узбекистан"in name_country,
                "таджикистан"in name_country, 
                "российская федерация" in name_country,
                "беларусь" in name_country, 
                "казахстан" in name_country, 
                "киргизстан" in name_country, 
                "узбекистан" in name_country, 
                "таджикистан" in name_country, 
                "беларусь" in name_country, 
                "казахстан" in name_country, 
                "киргизстан" in name_country, 
                "узбекистан" in name_country, 
                "таджикистан" in name_country, 
                "кндр" in name_country, 
                "корейская народная демократическая республика" in name_country])>=1:
                if name_country in countries:
                    count_otec+=0
                else:
                     count_otec+=1
                     countries.append(name_country)
    return count_otec


def count_city():#функция подсчёта городов
    count_town=0#подсчет городов
    cities=[]#массив со всеми городами(без повторов)
    column_city=database.give_column("city")#массив со всеми городами
    for i in column_city:
        i=i.lower()
        if i in cities:
            count_town+=0
        else:
            count_town+=1
            cities.append(i)
    return count_town


def count_geoobj():#функция подсчёта посещенных мест
    count_places=0#подсчет посещенных мест
    places=[]#массив со всеми посещенными местами(без повторов)
    column_geoobj=database.give_column("geogr_obg")#массив со всеми посещенными местами
    for i in column_geoobj:
        i=i.lower()
        if i in places:
            count_places+=0
        else:
            count_places+=1
            places.append(i)
    return count_places