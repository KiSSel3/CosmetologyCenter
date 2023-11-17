const banners = document.querySelectorAll('.banner');
const startButton = document.getElementById('startRotation');
const stopButton = document.getElementById('stopRotation');
const rotationIntervalInput = document.getElementById('rotationInterval');
let currentBanner = 0;
let rotationInterval;

function rotateBanners() {
    banners[currentBanner].style.display = 'none';
    currentBanner = (currentBanner + 1) % banners.length;
    banners[currentBanner].style.display = 'block';
}

function startRotation() {
    stopRotation();
    const interval = parseInt(rotationIntervalInput.value) * 1000; 
    if (!rotationInterval) {
        rotationInterval = setInterval(rotateBanners, interval);
    }
    localStorage.setItem('interval', interval);
}

function stopRotation() {
    if (rotationInterval) {
        clearInterval(rotationInterval);
        rotationInterval = null;
    }
}

startButton.addEventListener('click', startRotation);
stopButton.addEventListener('click', stopRotation);

document.addEventListener('visibilitychange', function () {
    if (document.hidden) {
        stopRotation();
    } else {
        startRotation();
    }
});

startRotation();