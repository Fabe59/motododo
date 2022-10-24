popupCenter = function(url, title, width, height) {
    let popupWidth = width || 640;
    let popupHeight = height || 320;
    let top = window.screenTop || window.screenY;
    let left = window.screenLeft || window.screenX;
    let windowWidth = window.innerWidth || document.documentElement.clientWidth;
    let windowHeight = window.innerHeight || document.documentElement.clientHeight;
    let popupLeft = left + windowWidth / 2 - popupWidth / 2 ;
    let popupTop = top + windowHeight /2 - popupHeight / 2 ;
    window.open(url, title, 'scrollbars=yes, width=' + popupWidth + ', height=' + popupHeight + ', top=' + popupTop + ', left=' + popupLeft + '');
    }
    
document.querySelector(".button-twitter").addEventListener('click', function(e) {
    e.preventDefault();
    let url = this.getAttribute('data-url');
    let shareUrl = "https://twitter.com/intent/tweet?text=" + document.title + "&via=FabePrgt" + "&url=" + url;
    popupCenter(shareUrl, "Partager sur Twitter")
})

document.querySelector(".button-facebook").addEventListener('click', function(e) {
    e.preventDefault();
    let url = this.getAttribute('data-url');
    let shareUrl = "https://www.facebook.com/sharer/sharer.php?u=" + url;
    popupCenter(shareUrl, "Partager sur Facebook");   
})