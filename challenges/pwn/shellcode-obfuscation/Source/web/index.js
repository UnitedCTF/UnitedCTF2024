


execute = async (level) => {
    let button  = document.getElementById(`execute_button_${level}`)
    button.disabled = true
    let shellcode_box = document.getElementById(`level${level}_bytes`);
    shellcode_box.innerHTML = "";
    let shellcode = shellcode_box.value;
    res = await send_req(level, shellcode)
    let output_box = document.getElementById(`level${level}_output`);
    button.disabled = false
    if (res.error) {
        output_box.innerHTML = res.error;
        return;
    }
    output_box.innerHTML = res.flag;
}
send_req = async (level, shellcode) => {
    let res = await fetch(`/level${level}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            shellcode_bytes: shellcode
        })
    });
    return await res.json();
}