function start_w_i_i(){
    id = localStorage.getItem("line_id")
    console.log("id=", id)
    eel.give_line(id)(write_in_input)
}

function write_in_input(data){
    console.log("data="+data)
    country = document.getElementById("Name_Country")
    city = document.getElementById("Name_City")
    geogr_obg = document.getElementById("Name_geogr_obj")
    date_start = document.getElementById("start_date")
    date_end = document.getElementById("end_date")
    comment = document.getElementById("comment")
    ocenca = document.getElementById("ocenca_travel")
    active = document.getElementById("ocenca_active")

    let s_s = data[4].slice(6)+"-"+data[4].slice(3, 5)+"-"+data[4].slice(0, 2)
    let s_e = data[5].slice(6)+"-"+data[5].slice(3, 5)+"-"+data[5].slice(0, 2)
    console.log("getfullyear="+s_s, data[4])

    country.value = data[1]
    city.value = data[2]
    geogr_obg.value = data[3]
    date_start.value = data[4]
    date_end.value = data[5]
    comment.value = data[6]
    ocenca.value = data[7]
    active.value = data[8]
}

function change_data(){
    id = localStorage.getItem("line_id")
    country = document.getElementById("Name_Country").value
    city = document.getElementById("Name_City").value
    geogr_obg = document.getElementById("Name_geogr_obj").value
    date_start = document.getElementById("start_date").value
    date_end = document.getElementById("end_date").value
    comment = document.getElementById("comment").value
    ocenca = document.getElementById("ocenca_travel").value
    active = document.getElementById("ocenca_active").value
    // date_start = date_start.slice(8)+"-"+date_start.slice(5,7)+"-"+date_start.start(0, 4)
    // date_end = date_end.slice(8)+"-"+date_end.slice(5,7)+"-"+date_end.start(0, 4)
    eel.edit(id, country, city, geogr_obg, date_start, date_end, comment, ocenca, active)(f_close)
}

function f_close(){
    window.close()
}


function close_change_table_window(){
    window.close()
}