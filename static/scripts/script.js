function toogleMenu(){
    var menuToogle = document.getElementById("menutoggle");
    var navigation = document.getElementById("navigationId");
    menuToogle.classList.toggle('active')
    navigation.classList.toggle('active')
}

function onOff(){
    var toggleHide = document.getElementById("containerbx");
    toggleHide.classList.toggle('hide')
}