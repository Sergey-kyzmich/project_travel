function start_table(){
    eel.add_to_html_table()(add_to_table)
}

function add_to_table(res){
    console.log(res)
    data = res["data"]
    len_table = res["len_table"]
    for(i=1;i<=len_table;i++){
        console.log(data[i])
    const table_body = document.getElementById("table-body");
    let tr = document.createElement("tr");
    let td1 = document.createElement("td");
    let td2 = document.createElement("td");
    let td3 = document.createElement("td");
    let td4 = document.createElement("td");
    let td5 = document.createElement("td");
    let td6 = document.createElement("td");
    let td7 = document.createElement("td");
    let td8 = document.createElement("td");
    let td9 = document.createElement("td");

    td1.innerText = data[i-1][0];
    td2.innerText = data[i-1][1];
    td3.innerText = data[i-1][2];
    td4.innerText = data[i-1][3];
    td5.innerText = data[i-1][4];
    td6.innerText = data[i-1][5];
    td7.innerText = data[i-1][6];
    td8.innerText = data[i-1][7];
    td9.innerText = data[i-1][8];

    tr.appendChild(td1);
    tr.appendChild(td2);
    tr.appendChild(td3);
    tr.appendChild(td4);
    tr.appendChild(td5);
    tr.appendChild(td6);
    tr.appendChild(td7);
    tr.appendChild(td8);
    tr.appendChild(td9);
    table_body.appendChild(tr);
    }
    select_name_change_table()
}

function reload(){
    location.reload()
}

function select_name_change_table(){
    eel.len_db()(s_n_c_t)
}

function s_n_c_t(len){
    console.log("len table=" + len)
    const table_body_1 = document.getElementById('change_table_select');
    const table_body_2 = document.getElementById("change_delete_select")
    for(i = 0;i<len;i++){
        let td1 = document.createElement("option");
        td1.innerText = String(i+1);
        td1.value = String(i+1)
        table_body_1.appendChild(td1);
        table_body_2.appendChild(td1)
    }
}


function open_html(name_file){
    d = document.getElementById("change_table_select").value
    localStorage.setItem("line_id", d)
    localStorage.setItem("window_table_html", window)
    eel.open_html_file(name_file)
}

function delete_line(){
    id = document.getElementById("change_delete_select").value
    eel.delete(id)

}

function close_table_window(){
    window.close()
}