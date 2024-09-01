window.onload = function () {
    const tresor_challenge = document.getElementById('tresor');
    tresor_challenge.addEventListener('submit', (e) => {
        e.preventDefault();
        e.stopPropagation();

        var key = document.getElementById('key').value;
        var twoFA = document.getElementById('twoFA').value;
        console.log(twoFA)
        if (key === "captain") {
            fetch("/tresors/2", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json; charset=UTF-8'
                },
                body: JSON.stringify({
                    key,
                    twoFA,
                }),
            })
            .then((res) => {
                const jsonPromise = res.json();
                jsonPromise.then((data) => {
                    alert(data['flag']);
                });
            })
        } else {
            console.log(":(")
        }
    })
}