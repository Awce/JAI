from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core import serializers
from factura.models import Documento,Folio,Receptor,Ticket
from django.utils import simplejson
import json
from django.shortcuts import get_list_or_404, get_object_or_404
# Create your views here.

def index(request):
	errors = []
	doc = Documento.objects.filter(estatus=True)
	ser = Folio.objects.filter(serie="A")
	if request.method == 'POST':
		print "no implementado"
		return HttpResponse("no implementado")
	return render_to_response('index.html',{'errors':errors,'doc':doc,'ser':ser})

def wsInsertarProducto(request):
	print request
	if request.method == "GET":
		print request.GET['serie']
		#print request.GET['serie']
		if 'producto' in request.GET: 
		#request.GET['producto'] and request.GET['unidad'] and request.GET['cantidad'] and request.GET['precio'] :
			serie =request.GET['producto']
			folio = request.GET['folio']
			total =0;
			codigo="000"
			producto=request.GET['producto']
			unidad=request.GET['unidad']
			cantidad=request.GET['cantidad']
			precio=request.GET['precio']
			if request.GET['grava'] == 'grava':
				total = float(precio) * float(cantidad) * 1.16
			else:
				total = float(precio) * float(cantidad)
			
			ctx ={'precio':precio,'producto':producto,'unidad':unidad,'cantidad':cantidad,'total':total,'codigo':'000','respuesta':'OK'}
			data = json.dumps(ctx)
			t = Ticket()
			t.serie = serie
			t.folio=folio
			t.codigo=codigo
			t.producto=producto
			t.unidad=unidad
			t.cantidad=cantidad
			t.precio=precio
			t.total=total
			t.save()
			
		else:
			data = json.dumps({'respuesta':'failed'})
	return HttpResponse(data,mimetype='application/json')
	
def wsBuscarReceptor(request):
	if request.method == "GET":
		rfc = request.GET['rfc']

		if rfc !="":
			try:
				r = get_object_or_404(Receptor,rfc=rfc)		
				d={'razon':r.razon_social,'pais':r.pais,'estado':r.estado,'municipio':r.ciudad,'colonia':r.colonia,
				'calle':r.calle,'interior':r.numero_interior,'exterior':r.numero_exterior,'cp':r.codigo_postal,
				'correo':r.email,'referencia':r.referencia,'respuesta':'OK','rfc':r.rfc}
				data = 	json.dumps(d)	
				return  HttpResponse(data,mimetype='application/json')
			except:
				data = 	json.dumps({'respuesta':'fail'})
				return  HttpResponse(data,mimetype='application/json')


		else:
			data = 	json.dumps({'respuesta':'fail'})
			return  HttpResponse(data,mimetype='application/json')

			
		
		
def wsBuscarFolio(request):
	if request.method == "GET":
		if 'serie' in request.GET:
			s = str(request.GET['serie'])
			folio = Folio.objects.get(serie=s)
			data = json.dumps({'folio':str(folio.folio_actual),'respuesta':'OK'})
		else:
			data = json.dumps({'respuesta':'failed'})
	return HttpResponse(data,mimetype='application/json')

def autocompleteRfc(request):
    search_qs = Receptor.objects.filter(rfc__startswith=request.REQUEST['search'])
    results = []
    for r in search_qs:
        results.append(r.rfc)
    resp = request.REQUEST['callback'] + '(' + simplejson.dumps(results) + ');'
    return HttpResponse(resp, content_type='application/json')


