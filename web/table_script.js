function get_data(){
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
}