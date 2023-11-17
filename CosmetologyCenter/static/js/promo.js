function applyPromo(){

    const total_price = document.querySelector('.total_price');
            
    old_price = total_price.textContent.replace("$", "");
    old_price = old_price.replace(",", ".");

    old_price = Number(old_price);
    const promoInput = document.getElementById('dob');
    let discount = Number(promoInput.value);
    let new_price = ((100-discount) * old_price/100).toString();
    total_price.textContent = "$"+ new_price;
}