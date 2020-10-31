var x = 3;
var posx = x.toString();
var y = 4;
var posy = y.toString();    
var concat = posx + posy; 

console.log(concat);

$(document).ready(function(){
    $("#Q01").val();
    console.log("cambio en valor tabla");
});

function cambiar_ficha(concat){
    console.log(concat);
    console.log("paso");
    $(concat).removeClass('cell empty').addClass('cell white'); 

    $.ajax({
        type: 'POST',
        url: "/",
        data: JSON.stringify(concat),
        method: 'POST',
        contentType: "application/json;charset=utf-8",
        success: function(json) {
            console.log("success");
        },
        error: function(e) {
            console.log(e.message);
        }
    });
}

//$('#00').removeClass('cell empty').addClass('cell black');

