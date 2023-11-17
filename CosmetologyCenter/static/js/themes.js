// Функция для изменения размера шрифта
function changeFontSize() {
    const fontSize = document.getElementById('fontSize').value;
    document.body.style.fontSize = fontSize + 'px';
  }
  
  // Функция для изменения цвета текста
  function changeTextColor() {
    const textColor = document.getElementById('textColor').value;
    document.body.style.color = textColor;
  }
  
  // Функция для изменения цвета фона страницы
  function changeBackgroundColor() {
    const bgColor = document.getElementById('bgColor').value;
    document.body.style.backgroundColor = bgColor;
  }
  