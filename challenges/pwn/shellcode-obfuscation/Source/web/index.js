


execute = async (level) =>{
    var shellcode_box = document.getElementById(`level${level}_bytes`);
    shellcode_box.innerHTML = "";
    var shellcode = shellcode_box.value;
    var operation_box = document.getElementById(`level${level}_operations`);
    var operation = ""
    if(operation_box !== undefined && operation_box !== null){
        operation = operation_box.value;
    }
    res = await send_req(level,shellcode,operation)
    var output_box = document.getElementById(`level${level}_output`);
    if(res.error){
        output_box.innerHTML = res.error;
        return;
    }
    output_box.innerHTML = res.flag;
}
send_req = async (level,shellcode,operation) =>{
    var res = await fetch(`/level${level}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            shellcode_bytes: shellcode,
            operation: operation
        })
    });
    return await res.json();
}

operation = (level) =>{
    var operation_box = document.getElementById(`level${level}_operations`);
    var operation = operation_box.value;
    var operation_output_box = document.getElementById(`level${level}_op_output`);
    var shellcode_box = document.getElementById(`level${level}_bytes`);
    var shellcode = shellcode_box.value;
    operation_output_box.innerHTML = `[${operation} for x in b"${shellcode}"]`;
}
init = () =>{
    var operation_box2 = document.getElementById(`level2_operations`);
    operation_box2.addEventListener('input', () => {
        operation(2);
    });
    var operation_box3 = document.getElementById(`level3_operations`);
    operation_box3.addEventListener('input', () => {
        operation(3);
    });
}
setTimeout(init, 100);