function startTimer() {
    const endTime = new Date().getTime() + 3600000; 
    localStorage.setItem('timerEndTime', endTime);
    updateTimer();
  }
  
  function updateTimer() {
    const endTime = parseInt(localStorage.getItem('timerEndTime'));
    if (!endTime) {
      startTimer();
      return;
    }
  
    const currentTime = new Date().getTime();
    const timeRemaining = endTime - currentTime;
  
    if (timeRemaining <= 0) {
      document.getElementById('countdown').textContent = 'Время истекло';
      localStorage.removeItem('timerEndTime');
    } else {
      const hours = Math.floor(timeRemaining / 3600000);
      const minutes = Math.floor((timeRemaining % 3600000) / 60000);
      const seconds = Math.floor((timeRemaining % 60000) / 1000);
  
      const timerDisplay = `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
      document.getElementById('countdown').textContent = timerDisplay;
      setTimeout(updateTimer, 1000);
    }
  }

  const endTime = localStorage.getItem('timerEndTime');
  if (endTime) {
    updateTimer();
  } else {
    startTimer();
  }
