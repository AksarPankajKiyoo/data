
var count = 0;
var clickBtn = document.getElementById('clickBtn');
clickBtn.addEventListener('click', ()=>{
    count++;
    if(count==1){
        document.getElementById('image').src = "https://www.angrybirds.com/wp-content/uploads/2022/05/optimized-ABCOM_202203_1000x1000_CharacterDimensio_Hatclings_Movie.png";
    }
    else {
        document.getElementById('image').src = "https://imgv3.fotor.com/images/slider-image/A-clear-image-of-a-woman-wearing-red-sharpened-by-Fotors-image-sharpener.jpg";
        count = 0;
    }
})