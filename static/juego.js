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

//se traduce de 0 y 1, y se reemplaza a clase de html
function actualizar_tablero(tabla_de_actualizacion, tipo_tablero){
    for(var i = 0; i< 6; i++){
        for(var j = 0; j< 6; j++){
            if (parseInt(tabla_de_actualizacion[tipo_tablero][i][j]) == 0){
                $('#'+i +''+j).removeClass().addClass('cell empty');
                $('#'+i +''+j).removeAttr("onclick");
            }
            if (parseInt(tabla_de_actualizacion[tipo_tablero][i][j]) == 2){
                $('#'+i +''+j).removeClass().addClass('cell white');
                $('#'+i +''+j).removeAttr("onclick");
            }
            if (parseInt(tabla_de_actualizacion[tipo_tablero][i][j]) == 1){
                $('#'+i +''+j).removeClass().addClass('cell black');
                $('#'+i +''+j).removeAttr("onclick");
            }
            if (parseInt(tabla_de_actualizacion[tipo_tablero][i][j]) == -1){
                $('#'+i +''+j).removeClass().addClass('cell black attackable');
                $('#'+i +''+j).attr('onclick', 'cambiar_ficha('+'"'+'#'+i +''+j+''+'"'+')');
            }
            if (parseInt(tabla_de_actualizacion[tipo_tablero][i][j]) == -2){
                $('#'+i +''+j).removeClass().addClass('cell white attackable');
                $('#'+i +''+j).attr('onclick', 'cambiar_ficha('+'"'+'#'+i +''+j+''+'"'+')');
            }
        }
    }
}
    

function iniciar_juego(jugador){
    var dificultad = $( "#dificultad").val();
    var tablero = matriz_completa()
    if(dificultad != 'vacio'){
        var envio = {"espero": "inicio_juego","ficha jugada" : jugador,"tablero" : tablero, "dificultad" : dificultad };
        console.log(dificultad)
        $( "#titulo" ).empty();
        $( "#titulo" ).append( "Nivel: "+dificultad+"");

    }
    else{
        var envio = {"espero": "inicio_juego","ficha jugada" : jugador,"tablero" : tablero};
    }
    $.ajax({
        type: 'POST',
        url: "/receiver",
        data: JSON.stringify(envio),
        method: 'POST',
        contentType: "application/json;charset=utf-8",
        success: function(json) {
            console.log("success");
            $('#exampleModal').modal('hide')
            $("#botones").fadeOut( "slow" );
            if(json['turno'] == "Te toca"){
                setTimeout(function(){
                    $("#ayuda").fadeIn("slow");
                }, 500);
            }
            $("#turno_jugador").append(json['turno']);
            console.log(json['turno'])
            console.log(json['tablero_espera'])
            actualizar_tablero(json, 'tablero_espera')
        },
        error: function(e) {
            console.log(e.message);
        }
    });
}

//envia ayuda
function movimiento_ayuda(){
    var turno = $("#turno_jugador").text();
    var dificultad = $("#titulo").text();
    var tablero = matriz_completa();
    var envio = {"espero": "ayuda","ficha jugada" : concat,"tablero" : tablero, "turno jugador" : "", "dificultad" : dificultad };

        $.ajax({
            type: 'POST',
            url: "/receiver",
            data: JSON.stringify(envio),
            method: 'POST',
            contentType: "application/json;charset=utf-8",
            success: function(json) {
                console.log(json['mov_ayuda'][0])
                cord_x= json['mov_ayuda'][0]+1
                cord_y= transforma_num_a_letra(json['mov_ayuda'][1]+1)
                createToast('Movimiento recomendado', cord_x+" "+cord_y);
            
            

            },
            error: function(e) {
                console.log(e.message);
            }
        });
}

function transforma_num_a_letra(num){

    switch(num)
    {
        case 1: return 'a';
        case 2: return 'b';
        case 3: return 'c';
        case 4: return 'd';
        case 5: return 'e';
        case 6: return 'f';
    }

    return '';
}//Unidades()

//RECIBIR VARIOS tableros
function cambiar_ficha(concat){
    var turno = $("#turno_jugador").text();
    var dificultad = $("#titulo").text();
    console.log(dificultad)
    var tablero = matriz_completa();
    var envio = {"espero": "jugada humano","ficha jugada" : concat,"tablero" : tablero, "turno jugador" : turno, "dificultad" : dificultad };
   
    if(turno == "Te toca" || turno == "Turno Maquina"){
        $('#spin').removeAttr('hidden');
        $('#spin').show();
        $('#ayuda').attr('disabled', true);



        $.ajax({
            type: 'POST',
            url: "/receiver",
            data: JSON.stringify(envio),
            method: 'POST',
            contentType: "application/json;charset=utf-8",
            success: function(json) {
                actualizar_tablero(json, 'tablero_espera')
                $("#turno_jugador").empty();
                $("#turno_jugador").append(json['turno']);    
                console.log("primero")
                if(json['turno'] =="El juego ha terminado"){
                    $("#titulo-quien-gano").empty();
                    $("#parrafo-quien-gano").empty();
                    $("#puntaje-quien-gano").empty();
                    $("#titulo-quien-gano").append("Finish");  
                    $("#parrafo-quien-gano").append(json['ganador']);  
                    $("#puntaje-quien-gano").append(`Con un puntaje de: ${json['puntaje_negro']} fichas Negras VS ${json['puntaje_blanco']} Fichas blancas`);  
                    
                    $('#exampleModal2').modal('show');
                    
                }
            },
            error: function(e) {
                console.log(e.message);
            }
        });
        
        var turno2 ="Turno Maquina"
        var dificultad = $("#titulo").text();
        setTimeout(function(){
            var tablero = matriz_completa();
    
        
            console.log(tablero)
            var mini = {"espero": "jugada humano","tablero" : tablero, "turno jugador" : turno2, "dificultad" : dificultad  };
            console.log("llegamos")
            $.ajax({
                type: 'POST',
                url: "/receiver",
                data: JSON.stringify(mini),
                method: 'POST',
                contentType: "application/json;charset=utf-8",
                success: function(json) {
                    $('#spin').hide();
                    $('#ayuda').prop("disabled", false); 
                    actualizar_tablero(json, 'tablero_espera')
                    $("#turno_jugador").empty();
                    $("#turno_jugador").append(json['turno']);
                    console.log("segundo")
                    if(json['turno'] =="El juego ha terminado"){
                        $("#titulo-quien-gano").empty();
                        $("#parrafo-quien-gano").empty();
                        $("#puntaje-quien-gano").empty();
                        $("#titulo-quien-gano").append("Finish");  
                        $("#parrafo-quien-gano").append(json['ganador']);  
                        $("#puntaje-quien-gano").append(`Con un puntaje de: ${json['puntaje_negro']} fichas Negras VS ${json['puntaje_blanco']} Fichas blancas`);  
                        
                        $('#exampleModal2').modal('show');
                        
                    }
                },
                error: function(e) {
                    console.log(e.message);
                }
            });

        }, 1000);
    
    
    }else{
        $.ajax({
            type: 'POST',
            url: "/receiver",
            data: JSON.stringify(envio),
            method: 'POST',
            contentType: "application/json;charset=utf-8",
            success: function(json) {
                console.log("success");
                console.log(json['turno'])
                console.log(json['tablero_espera'])
                if(json['turno'] =="El juego ha terminado"){
                    $("#titulo-quien-gano").empty();
                    $("#parrafo-quien-gano").empty();
                    $("#puntaje-quien-gano").empty();
                    $("#titulo-quien-gano").append("Finish");  
                    $("#parrafo-quien-gano").append("Han ganado las fichas "+json['ganador']);  
                    $("#puntaje-quien-gano").append(`Con un puntaje de: ${json['puntaje_negro']} fichas Negras VS ${json['puntaje_blanco']} Fichas blancas`);  
                    
                    $('#exampleModal2').modal('show');
                    
                }
                actualizar_tablero(json, 'tablero_espera')
                $("#turno_jugador").empty();
                $("#turno_jugador").append(json['turno']);
                if(typeof json['mensaje'] != 'undefined'){
                    $('#mensajeSuccess').html(json['mensaje']);
                    $('#alertSuccess').fadeIn( "slow" )
                    setTimeout(function(){
                        $('#alertSuccess').fadeOut( "slow" );
                    }, 1500);
                    
                }
    
            },
            error: function(e) {
                console.log(e.message);
            }
        });

    }
   
    
}






function getBoard() {
    var board = [];
    var tds = document.getElementsByTagName('td');
    for (var i = 0; i < tds.length; i += 1) {
      board.push(tds[i].className);
    }
    return board;
}
//trae matriz para enviar
function matriz_completa(){
    var tablero = getBoard();
    var tds = document.getElementsByTagName('td');
    var bolos = [];
    var salida = [];
    for(var i = 0; i< 36; i++){
        bolos.push(tablero[i]);
        if(i == 5 || i == 11 || i == 17 || i == 23 || i == 29 || i == 35){
            salida.push(bolos);
            bolos = [];
        }
    }

    return salida;
     
}




  
  function createToast(title, text) {
    let id = new Date().getTime();
    let html = `<div role="alert" aria-live="assertive" aria-atomic="true" class="toast" data-autohide="false" id=${id} >
                  <div class="toast-header">
                      <svg class="ounded mr-2" width="20" height="20" xmlns="http://www.w3.org/2000/svg"
                      preserveAspectRatio="xMidYMid slice" focusable="false" role="img">
                      <rect fill="#007aff" width="100%" height="100%" /></svg>
                      <strong class="mr-auto">${title}  </strong>
                      <small> *Consejos</small>
                      <button type="button" class="ml-2 mb-1 close" data-dismiss="toast" aria-label="Close">
                      <span aria-hidden="true">&times;</span>
                      </button>
                  </div>
                  <div class="toast-body">
                      ${text}
                  </div>
              </div>`;
  
    document.getElementById('toast-container').innerHTML += html;
            $(`#${id}`).toast('show');

  }

  $('body').on('click','.close',function(){
    $(this).closest('.toast').toast('hide')
  })



//$('#00').removeClass('cell empty').addClass('cell black');

