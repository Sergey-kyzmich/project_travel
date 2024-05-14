function ch_error(){
    console.log("Запуск функции сохранения")
    co = document.getElementById("Name_Country")
    ci = document.getElementById("Name_City")
    ge = document.getElementById("Name_geogr_obj")
    ds = document.getElementById("start_date")
    de = document.getElementById("end_date")
    com = document.getElementById("comment")
    oc = document.getElementById("ocenca_travel")
    ac = document.getElementById("ocenca_active")

    country = co.value
    city = ci.value
    geogr_obg = ge.value
    date_start = ds.value
    date_end = de.value
    comment = com.value
    ocenca = oc.value
    active = ac.value
    eel.check_error(country, city, geogr_obg, date_start, date_end, comment, ocenca, active)(write_data)
}

function write_data(error){
    console.log("go")
    co = document.getElementById("Name_Country")
    ci = document.getElementById("Name_City")
    ge = document.getElementById("Name_geogr_obj")
    ds = document.getElementById("start_date")
    de = document.getElementById("end_date")
    com = document.getElementById("comment")
    oc = document.getElementById("ocenca_travel")
    ac = document.getElementById("ocenca_active")

    country = co.value
    city = ci.value
    geogr_obg = ge.value
    date_start = ds.value
    date_end = de.value
    comment = com.value
    ocenca = oc.value
    active = ac.value

    console.log(error)
    text_warn = "Вы уверенны, что хотите сохранить запись?"
    if(error!=[]){
        text_warn+="\nОшибки:\n"
        for(i=0;i<error.length;i++){
            text_warn+=error[i]
        }
    }
    if(confirm(text_warn)){
    co.value = ""
    ci.value = ""
    ge.value = ""
    ds.value = ""
    de.value = ""
    com.value = ""
    oc.value = ""
    ac.value = ""
    eel.write_to_db(country, city, geogr_obg, date_start, date_end, comment, ocenca, active)
    }
}

function open_table_html(name_file){
    eel.open_html_file(name_file)
}


function close_main_window(){
    console.log("закрыть основной файл")
    window.close()
}

