# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Emisor(models.Model):

    def key_path(self,filename):
        path= "Archivos/Llave/%s/%s"%(self.rfc,str(filename))
        return path

    def cer_path(self,filename):
        path= "Archivos/Certificado/%s/%s"%(self.rfc,str(filename))
        return path

    def logo_path(self,filename):
        path= "Archivos/Logo/%s/%s"%(self.rfc,str(filename))
        return path

    usuario = models.OneToOneField(User)
    razon_social = models.CharField(max_length=255)
    rfc = models.CharField(max_length=13,unique=True)
    regimen_fiscal =models.CharField(max_length=255,blank=True,null=True)
    calle = models.CharField(max_length=255,blank=True,null=True)
    numero_exterior=models.CharField(max_length=10,blank=True,null=True)
    numero_interior=models.CharField(max_length=10,blank=True,null=True)
    colonia = models.CharField(max_length=255,blank=True,null=True)
    estado = models.CharField(max_length=255,blank=True,null=True)
    municipio = models.CharField(max_length=255,blank=True,null=True)
    codigo_postal = models.CharField(max_length=10,blank=True,null=True)
    telefono = models.CharField(max_length=10,blank=True,null=True)
    lugar_de_expedicion = models.CharField(max_length=255,blank=True,null=True)
    archivo_clave_privada = models.FileField(upload_to=key_path,null=True,blank=True)
    certificado = models.FileField(upload_to=cer_path,null=True,blank=True)
    clave_certicado = models.CharField(max_length=100,null=True,blank=True)
    logotipo = models.ImageField(upload_to=logo_path,null=True,blank=True)

    def __unicode__(self):
        return self.rfc


class Documento(models.Model):
    TIPO_DOCUMENTO=(
    	('I','INGRESO'),
		('E','EGRESO'),
		('T','TRASLADO'),
		)
    TIPO_IMPUESTO=(
        ('IVA','IVA'),
        ('IETU','IETU'),
        )
    TIPO_EFECTO=(('TRASLADADO','TRASLADADO'),('RETENIDO','RETENIDO'),)
    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=255,choices=TIPO_DOCUMENTO)
    efecto = models.CharField(max_length=10,choices=TIPO_EFECTO)
    impuesto = models.CharField(max_length=10,choices=TIPO_IMPUESTO)
    tasa = models.IntegerField()
    estatus = models.BooleanField()

    def __unicode__(self):
    	return self.nombre


class Servicio(models.Model):
    UNIDAD = (('NO APLICA','NO APLICA'),)
    codigo = models.CharField(max_length=10)
    unidad = models.CharField(max_length=30,choices=UNIDAD)#*
    descripcion = models.CharField(max_length=255)#*
    precio_unitario = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)

    def __unicode__(self):
        return self.descripcion

class Receptor(models.Model):
    rfc = models.CharField(max_length=13) #*
    razon_social = models.CharField(max_length=255) #*
    pais = models.CharField(max_length=255)#*
    estado = models.CharField(max_length=255,blank=True,null=True)
    ciudad = models.CharField(max_length=255,blank=True,null=True)
    colonia = models.CharField(max_length=255,blank=True,null=True)
    calle = models.CharField(max_length=255,blank=True,null=True)
    numero_exterior = models.CharField(max_length=10,blank=True,null=True)
    numero_interior = models.CharField(max_length=10,blank=True,null=True)
    codigo_postal = models.CharField(max_length=10,blank=True,null=True)
    email= models.EmailField(max_length=75,blank=True,null=True)
    telefono = models.CharField(max_length=15,blank=True,null=True)
    referencia = models.CharField(max_length=255,blank=True,null=True)

    def __unicode__(self):
        return self.rfc

class Sucursal(models.Model):
    nombre_de_la_sucursal = models.CharField(max_length=255) #*
    calle = models.CharField(max_length=255) #*
    numero_exterior = models.CharField(max_length=10,blank=True,null=True)
    numero_interior = models.CharField(max_length=10,blank=True,null=True)
    colonia = models.CharField(max_length=10,blank=True,null=True)
    estado = models.CharField(max_length=255)#*
    municipio = models.CharField(max_length=255)#*
    ciudad = models.CharField(max_length=255)#*
    codigo_postal = models.CharField(max_length=10)#*
    email= models.CharField(max_length=75,blank=True,null=True)
    telefono = models.CharField(max_length=10,blank=True,null=True)
    referencia = models.CharField(max_length=10,blank=True,null=True)

    def __unicode__(self):
        return self.nombre_de_la_sucursal


class Folio(models.Model):
    serie = models.CharField(max_length=10)
    folio_inicial = models.IntegerField(max_length=10) #*
    folio_final = models.IntegerField(max_length=10)#*
    folio_actual = models.IntegerField(max_length=10)#*

    def __unicode__(self):
        return self.serie



class Factura(models.Model):

    def xml_path(self,filename):
        path= "Archivos/XML/%s/%s"%(self.receptor.rfc,str(filename))
        return path

    ESTATUS=(
		('TIMBRADO','TIMBRADO'),
		('PENDIENTE','PENDIENTE'),
		('CANCELADO','CANCELADO'),
		)
    estatus = models.CharField(max_length=10,choices=ESTATUS)
    receptor=models.OneToOneField(Receptor)
    timbre_fiscal = models.CharField(max_length=255,blank=True)
    xml = models.FileField(upload_to=xml_path,blank=True,null=True)
    folio = models.IntegerField(max_length=10)

    def __unicode__(self):
    	return str(self.folio)

class Ticket(models.Model):
	serie = models.CharField(max_length=10)
	folio = models.IntegerField(max_length=10)
	codigo = models.CharField(max_length=255)
	producto = models.CharField(max_length=10)
	unidad = models.CharField(max_length=50)
	cantidad = models.DecimalField(max_digits=10,decimal_places=2)
	precio = models.DecimalField(max_digits=10,decimal_places=2)
	total = models.DecimalField(max_digits=10,decimal_places=2)
	
	def __unicode__(self):
		return str(self.id)
	
	
