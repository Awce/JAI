function Serie(){
	var serie = $('#serie').val();
	$.ajax({
		type:"GET",
		contentType:"application/json;charset=utf-8",
		dateType:"json",
		data:{'serie':serie},
		url:"/ws/buscar/folio/",
		success:function(response){
			if(response.respuesta == 'OK'){
				$('#folio').val(response.folio);
			}else{
				alert("no se existe serie de folio");
				}
			}
		});
}


function DatosReceptor(){
	//$('#searchRfc').on('focusout',function(e){
		var rfc = $('#searchRfc').val();
		$.ajax({
			type:"GET",
			contentType:"application/json;charset=utf-8",
			dateType:"json",
			data:{'rfc':rfc},
			url:"/ws/buscar/receptor/",
			success:function(response){
				llenarReceptor(response);
				}
			
			});
		}
function llenarReceptor(response){
	for( var r in response){
		if (response.respuesta == "OK"){
			if (r != "respuesta"){
				$('#'+r).val(response[r]);
				}
		}else{
			$('#'+r).val("");
		}
	}
}

function InsertarProducto(){
		var serie = $('#serie').val();
		var folio = $('#folio').val();
		var codigo = $('codigo').val();
		var formproduct =$('#producto').serializeArray();
		formproduct.push({name:'serie',value:serie});
		formproduct.push({name:'folio',value:folio});
		var c,u,d,p,t;
		var row="";
		$.ajax({
			type:"GET",
			contentType:"application/json;charset=utf-8",
			dateType:"json",
			data:formproduct,
			//data:$('#producto').serialize(),
			url:"/ws/insertar/producto/",
			success:function(response){
			if(response.respuesta == 'OK'){
				c = '<td>'.concat(response.codigo).concat('</td>');
				u = '<td>'.concat(response.unidad).concat('</td>');
				d = '<td>'.concat(response.producto).concat('</td>');
				p = '<td>'.concat(response.precio).concat('</td>');
				t = '<td>'.concat(response.total).concat('</td>').concat('<td>X</td>');
				var ini ='<tr>';
				var fin = '</tr>';
				var row = ini.concat(c).concat(u).concat(d).concat(p).concat(t).concat(fin);
				//alert(response.saludo);
				$("#TablaVentas tbody").prepend(row);
				$('#s').empty();
				$('#i').empty();
				$('#t').empty();
				$('#s').append('<strong>$'+response.subtotal+'</strong>');
				$('#i').append('<strong>$'+response.iva+'</strong>');
				$('#t').append('<strong>$'+response.ttal+'</strong>');
			}else{
				alert("no se pudo añadir el producto");
				}
			}
		});
}


function searchOpen() {
    var search = $('#searchRfc').val()
    var data = {
        search: search
    };
    $.ajax({
        url: '/ws/search/json/',
        data: data,
        dataType: 'jsonp',
        jsonp: 'callback',
        jsonpCallback: 'searchResult'
    });
}


function searchResult(data) {
    $( "#searchRfc" ).autocomplete ({
        source: data
    });
}
