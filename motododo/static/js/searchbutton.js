let inputbox1 = document.querySelector('#searchbox1');
let button1 = document.querySelector("#searchbutton1");
let inputbox2 = document.querySelector('#searchbox2');
let button2 = document.querySelector("#searchbutton2");

inputbox1.addEventListener("keyup", displayButton1);
inputbox2.addEventListener("keyup", displayButton2);

function displayButton1() {
  if(inputbox1.value == ""){
   button1.value = "Tous les hébergements";
  }else{
   button1.value = "Lancer la recherche";
  }
}

function displayButton2() {
    if(inputbox2.value == ""){
     button2.value = "Tous les hébergements";
    }else{
     button2.value = "Lancer la recherche";
    }
  }

displayButton1();
displayButton2();