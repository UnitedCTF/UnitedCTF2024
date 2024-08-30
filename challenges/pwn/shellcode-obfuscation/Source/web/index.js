


execute = async (level) => {
    const BYTES_PLACEHOLDER = "\"BYTES\""
    let shellcode_box = document.getElementById(`level${level}_bytes`);
    shellcode_box.innerHTML = "";
    let shellcode = shellcode_box.value;
    let operation_box = document.getElementById(`level${level}_operations`);
    let operation = ""
    if (operation_box !== undefined && operation_box !== null) {
        operation = `[${operation_box.value} for x in b${BYTES_PLACEHOLDER}]`;
        console.log(operation);
    }
    res = await send_req(level, shellcode, operation)
    let output_box = document.getElementById(`level${level}_output`);
    if (res.error) {
        output_box.innerHTML = res.error;
        return;
    }
    output_box.innerHTML = res.flag;
}
send_req = async (level, shellcode, operation) => {
    let res = await fetch(`/level${level}`, {
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

operation = (level) => {
    let operation_box = document.getElementById(`level${level}_operations`);
    let operation = operation_box.value;
    let operation_output_box = document.getElementById(`level${level}_op_output`);
    let shellcode_box = document.getElementById(`level${level}_bytes`);
    let shellcode = shellcode_box.value;
    operation_output_box.innerHTML = `[${operation} for x in b"${shellcode}"]`;
}
init = () => {
    let op2 = () => {
        operation(2);
    }

    let operation_box2 = document.getElementById(`level2_operations`);
    let shellcode_box2 = document.getElementById(`level2_bytes`);
    operation_box2.addEventListener('input', op2);
    shellcode_box2.addEventListener('input', op2);
}
setTimeout(init, 100);