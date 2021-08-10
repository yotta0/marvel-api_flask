function toogleMenu(){
    var menuToogle = document.getElementById("menutoggle");
    var navigation = document.getElementById("navigationId");
    menuToogle.classList.toggle('active')
    navigation.classList.toggle('active')
}

function onOff(){
    var toggleHide = document.getElementById("containerbx");
    var backOpacity = document.getElementById("mainDiv");
    toggleHide.classList.toggle('hide')
    backOpacity.classList.toggle('transparent')
}
