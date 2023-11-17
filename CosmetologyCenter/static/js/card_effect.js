const cards = document.querySelectorAll('.card');
for(let i = 0; i<cards.length; i++){
    const card = cards[i];
    card.addEventListener('mousemove', start_rotate);
    card.addEventListener('mouseout', stop_rotate);

}
function start_rotate(event){
    const card_item = this.querySelector('.card-item');
    console.log(card_item);
    const half_height =card_item.offsetHeight / 2;
    const half_width =card_item.offsetWidth / 2;
    card_item.style.transform = 'rotateX(' + -(event.offsetY-half_height)/12+ 'deg) rotateY('+ (event.offsetX - half_width) / 12+'deg)'
}

function stop_rotate(event){
const card_item = this.querySelector('.card-item');
card_item.style.transform = 'rotate(0)'

}