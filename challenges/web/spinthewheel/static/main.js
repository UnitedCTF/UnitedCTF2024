const spinBtn = document.getElementById('spin-btn');
const wheel = document.getElementById('wheel');
const balance = document.getElementById('balance');

if(spinBtn) {
    spinBtn.addEventListener('click', async _ => {
        const res = await fetch('/spin', {method: 'POST'});
        if(res.ok) {
            const data = await res.json();
            const newAngle = 1800 - 270 - data.wheel_choice * 30 + (Math.random() - 0.5) * 30;
            wheel.style.transform = `rotate(${newAngle}deg)`;

            setTimeout(() => {
                const confetti = new Confetti('wheel');
                confetti.setCount(100);
                confetti.setSize(1.5);
                confetti.setPower(25);
                confetti.destroyTarget(false);

                balance.innerText = `${data.new_balance}$`;

                setTimeout(() => {
                    const wheelRect = wheel.getBoundingClientRect();
                    wheel.dispatchEvent(new MouseEvent('click', {clientX: wheelRect.x + wheelRect.width / 2, clientY: wheelRect.y + wheelRect.height / 2}));
                    confetti.setCount(0);
                    
                    Toastify({
                        text: `Bravo! Vous avez gagné: ${wheel.children[data.wheel_choice].innerText}`,
                        duration: 3000,
                        newWindow: true,
                        close: false,
                        gravity: 'bottom',
                        position: 'center',
                        stopOnFocus: true
                    }).showToast();
                }, 10);
            }, 4000);
        } else {
            alert('Oopsie doopsie, vous avez déjà fait tourner la roue cette semaine...');
        }
    });
}