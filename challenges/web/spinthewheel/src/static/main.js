const spinBtn = document.getElementById('spin-btn');
const wheel = document.getElementById('wheel');
const balance = document.getElementById('balance');

if(spinBtn) {
    spinBtn.addEventListener('click', async _ => {
        spinBtn.setAttribute('disabled', 'disabled');

        wheel.style.transition = 'none';
        wheel.style.transform = 'rotate(0deg)';

        const res = await fetch('/spin', {method: 'POST'});
        const data = await res.json();

        setTimeout(() => {
            const newAngle = 1800 - 270 - data.wheel_choice * 30 + (Math.random() - 0.5) * 30;
            wheel.style.transition = 'transform 4s cubic-bezier(0, 0.5, 0.5, 1)';
            wheel.style.transform = `rotate(${newAngle}deg)`;
        }, 10);

        setTimeout(() => {
            const confetti = new Confetti('wheel');
            confetti.setCount(100);
            confetti.setSize(1.5);
            confetti.setPower(25);
            confetti.destroyTarget(false);

            spinBtn.removeAttribute('disabled');
            balance.innerText = `${data.new_balance}$`;

            setTimeout(() => {
                const wheelRect = wheel.getBoundingClientRect();
                wheel.dispatchEvent(new MouseEvent('click', {clientX: wheelRect.x + wheelRect.width / 2, clientY: wheelRect.y + wheelRect.height / 2}));
                confetti.setCount(0);
                
                let message;
                if([0, 4, 9].includes(data.wheel_choice)) {
                    message = 'Oh non! Vous avez tout perdu... 😢';
                } else {
                    message = `Bravo! Vous avez gagné ${wheel.children[data.wheel_choice].innerText.toLowerCase()}! 🥳`;
                }

                Toastify({
                    text: message,
                    duration: 3000,
                    newWindow: true,
                    close: false,
                    gravity: 'bottom',
                    position: 'center',
                    stopOnFocus: true
                }).showToast();
            }, 10);
        }, 4000);
    });
}