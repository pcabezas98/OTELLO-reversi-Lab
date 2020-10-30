var x = 3;
var posx = x.toString();
var y = 4;
var posy = y.toString();    
var concat = posx + posy; 

console.log(concat);

function cambiar_ficha(concat){
    console.log(concat);
    console.log("paso");
    $(concat).removeClass('cell empty').addClass('cell white'); 
}

$('#00').removeClass('cell empty').addClass('cell black');

