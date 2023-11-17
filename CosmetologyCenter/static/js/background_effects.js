document.body.addEventListener('mousemove', function(event) {
    // Calculate the red value based on the mouse's X position
    const r = Math.round(255 * event.clientX / window.innerWidth);
    const g = Math.round(255 * event.clientY / window.innerHeight);
    // Calculate the blue value using the red and green values
    const b = Math.round(255 * (r + g) / 510);
    document.body.style.backgroundColor = `rgb(${r}, ${g}, ${b})`;
});