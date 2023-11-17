const progress_bar = document.querySelector('.progress');

window.addEventListener('scroll', progress);

function progress(e){
    let window_scroll = document.body.scrollTop || document.documentElement.scrollTop;
    let window_height = document.documentElement.scrollHeight - document.documentElement.clientHeight;

    let percent = window_scroll/ window_height * 100;
    progress_bar.style.width = percent + '%';

} 