function write_data(){
    console.log("go")
    country = document.getElementById("Name_Country").value
    city = document.getElementById("Name_City").value
    geogr_obg = document.getElementById("Name_geogr_obj").value
    date_start = document.getElementById("start_date").value
    date_end = document.getElementById("end_date").value
    comment = document.getElementById("comment").value
    ocenca = document.getElementById("ocenca_travel").value
    active = document.getElementById("ocenca_active").value
    
    eel.write_to_db(country, city, geogr_obg, date_start, date_end, comment, ocenca, active)
}

function open_html(name_file){
    eel.open_html_file(name_file)
}


