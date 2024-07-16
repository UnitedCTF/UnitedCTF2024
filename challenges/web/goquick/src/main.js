const rideTimesCtn = document.getElementById('ride-times');
const jobStatusCtn = document.getElementById('job-status');

async function updateRideTimes() {
    const resp = await fetch('/data/rides.json');
    const rideTimes = await resp.json();
    
    rideTimesCtn.innerHTML = '';

    for(let ride of rideTimes) {
        rideTimesCtn.innerHTML += `
            <tr>
            <td>${ride.name}</td>
            <td>${ride.waitTime} minutes</td>
            <tr>
        `;
    }
}

async function updateJobStatus() {
    const resp = await fetch('/job-status.php');
    const job = await resp.json();

    if('id' in job) {
        jobStatusCtn.innerHTML = `<br><p class=\"${job.state}\">${job.result}</p><br>`;
    } else {
        jobStatusCtn.innerHTML = '';
    }
}

function update() {
    updateRideTimes();
    updateJobStatus();
}

setInterval(update, 5000);
update();