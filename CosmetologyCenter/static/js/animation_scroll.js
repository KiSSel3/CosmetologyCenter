window.addEventListener('scroll', function() {
    const scrollY = window.scrollY;
    const rightWoman = document.getElementById('right_woman');
    const leftWoman = document.getElementById('left_woman');
    const bottomWoman = document.getElementById('bottom_woman');
    const centerWoman = document.getElementById('center_woman');
  
    rightWoman.style.transform = `translateX(-${scrollY * 0.25}px)`;
    leftWoman.style.transform = `translateX(${scrollY * 0.25}px)`;
    bottomWoman.style.transform = `translateY(-${scrollY * 0.25}px)`;
    centerWoman.style.transform = `translate(-${scrollY * 0.125}px, -${scrollY * 0.125}px)`;
  });