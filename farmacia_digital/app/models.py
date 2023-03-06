from django.db import models


#-----------------------------------------------------------------------------------------------------------------#
#TABLA DE REGION
class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre_region = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre_region
    
#-----------------------------------------------------------------------------------------------------------------#
    
#TABLA DE PROVINCIA
class Provincia(models.Model):
    id_provincia = models.AutoField(primary_key=True)
    nombre_provincia = models.CharField(max_length=100)
    id_region =models.ForeignKey(Region, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre_provincia   

#-----------------------------------------------------------------------------------------------------------------# 
    
#TABLA DE COMUNA
class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombre_comuna = models.CharField(max_length=100)
    id_provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre_comuna
    
#-----------------------------------------------------------------------------------------------------------------#

#TABLA LABORATORIO
class Laboratorio(models.Model):
    id_laboratorio = models.AutoField(primary_key=True)
    nombre_laboratorio = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_laboratorio

#-----------------------------------------------------------------------------------------------------------------#

#TABLA DE PRINCIPIO ACTIVO
class Principio(models.Model):
    id_principio_activo= models.AutoField(primary_key=True)
    nombre_princio_activo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_princio_activo        

#-----------------------------------------------------------------------------------------------------------------#

#TABLA DE ADMINISTRACION MEDICAMENTO
class ViaAdminstracion(models.Model):
    id_via_administracion = models.AutoField(primary_key=True)
    nombre_via_administracion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_via_administracion

#-----------------------------------------------------------------------------------------------------------------#

#TABLA DE FARMACIA
class Farmacia(models.Model):
    id_farmacia = models.AutoField(primary_key=True)
    marca_farmacia = models.CharField(max_length=200)

    def __str__(self):
        return self.marca_farmacia

#-----------------------------------------------------------------------------------------------------------------#

#TABLA DE SUCURSAL FARMACIA
class FarmaciaSucursal(models.Model):
    id_sucursal = models.AutoField(primary_key=True)
    id_farmacia = models.ForeignKey(Farmacia, on_delete=models.PROTECT)
    id_comuna = models.ForeignKey(Comuna, on_delete=models.PROTECT)
    id_region = models.ForeignKey(Region, on_delete=models.PROTECT)
    id_provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT)
    direccion_sucursal = models.CharField(max_length=200)
    telefono_sucursal = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.direccion_sucursal
    
#-----------------------------------------------------------------------------------------------------------------#

#TABLA DE MEDICAMENTOS
class Medicamentos(models.Model):
    id_medicamento = models.AutoField(primary_key=True)
    id_laboratorio = models.ForeignKey(Laboratorio, on_delete=models.PROTECT)
    id_principio_activo = models.ForeignKey(Principio, on_delete=models.PROTECT)
    nombre_comercial = models.CharField(max_length=100)
    gramaje = models.CharField(max_length=50)
    cantidad =models.IntegerField()
    presentacion =models.CharField(max_length=100)
    lote = models.CharField(max_length=200)
    id_via_administracion = models.ForeignKey(ViaAdminstracion, on_delete=models.PROTECT)
    fecha_vencimento = models.DateField()
    #imagen = models.ImageField(upload_to="medicamentos", null=True)

    def __str__(self):
        return self.nombre_comercial
    
#-----------------------------------------------------------------------------------------------------------------#
    
#TABLA DE DESCUENTOS MEDICAMENTOS
class MedicamentosDescuento(models.Model):
    id_descuento = models.AutoField(primary_key=True)
    id_medicamento = models.ForeignKey(Medicamentos, on_delete=models.PROTECT)
    id_farmacia = models.ForeignKey(Farmacia, on_delete=models.PROTECT)
    fecha_inicio_descuento = models.DateField()
    fecha_termino_descuento = models.DateField()
    descuento_porcentaje = models.IntegerField()

    def __str__(self):
        return self.id_descuento
    
#-----------------------------------------------------------------------------------------------------------------#

#TABLA DE MEDICAMENTO FICHA TECNICA
class MedicamentoFichaTecnica(models.Model):
    id_ficha_medicamento = models.AutoField(primary_key=True)
    nombre_comercial = models.ForeignKey(Medicamentos, on_delete=models.PROTECT)
    url_ficha = models.CharField(max_length=700)

    def __str__(self):
        return self.url_ficha
    
#-----------------------------------------------------------------------------------------------------------------#


#TABLA TIPO DE USURIO
class Tipo_usuario(models.Model):
    id_tipo_usuario = models.AutoField(primary_key=True)
    nombre_tipo_usuario =models.CharField(max_length=100)
    def __str__(self):
        return self.nombre_tipo_usuario  

#-----------------------------------------------------------------------------------------------------------------#

#TABLA USUARIO
class Usuario (models.Model):
    id_usuario = models.AutoField(primary_key=True)
    id_tipo_usuario = models.ForeignKey(Tipo_usuario, on_delete=models.PROTECT)
    num_run_usuario = models.CharField(max_length=12)
    nombres_usuario = models.CharField(max_length=100)
    apellido_paterno_usuario = models.CharField(max_length=100)
    appelido_materno_usuario = models.CharField(max_length=100)
    dirreccion_usuario = models.CharField(max_length=150)
    email_usuario = models.EmailField()
    telefono_usuario = models.IntegerField()
    celular_usuario = models.IntegerField()
    whatsapp_usuario = models.IntegerField()
    telegram_usuario = models.IntegerField()
    id_comuna = models.ForeignKey(Comuna, on_delete=models.PROTECT)
    id_region = models.ForeignKey(Region, on_delete=models.PROTECT)
    id_provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT)
    #id_familiar = models.ForeignKey(Familiar, on_delete=models.PROTECT)
    def __str__(self):
        return self.nombres_usuario
    
#-----------------------------------------------------------------------------------------------------------------#
    
#TABLA DE USUARIO RECETA
class UsuarioReceta(models.Model):
    id_receta_usuario = models.AutoField(primary_key=True)
    fecha_registro = models.DateField()
    id_usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    id_medicamento = models.ForeignKey(Medicamentos, on_delete=models.PROTECT)
    tiempo_tratamiento = models.CharField(max_length=100)
    frecuencia_dosis = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __date__ (self):
        return self.fecha_registro

#-----------------------------------------------------------------------------------------------------------------#

#TABLA DE FARMACO VIGILANCIA
class UsuarioFarmacoVigilancia(models.Model):
    id_farmaco = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    id_receta_usuario = models.ForeignKey(UsuarioReceta, on_delete=models.PROTECT)
    nombre_comercial = models.ForeignKey(Medicamentos, on_delete=models.PROTECT)
    horario_receta_1 = models.CharField(max_length=200)
    horario_receta_2 = models.CharField(max_length=200)

    def __str__ (self):
        return self.id_farmaco

#-----------------------------------------------------------------------------------------------------------------#

#LISTADO DE ENFERMEDADES CRONICAS
enfermades_cronicas = [
    [0,"Ninguna."],
    [1,"VIH/SIDA."],
    [2,"Insuficiencia Renal Crónica."],
    [3,"Hipertensión Arterial Primaria o Esencial en personas de 15 años y más."],
    [4,"Epilepsia no Refractaria en personas de 1 año y menores de 15 años."],
    [5,"Hemofilia."],
    [6,"Tratamiento médico en personas de 55 años y más con Artrosis de cadera y/o rodilla leve o moderada."],
    [7,"Fibrosis quística."],
    [8,"Artritis reumatoidea."],
    [9,"Diabetes Mellitus tipo 1."],
    [10,"Epilepsia en el adulto."],
    [11,"GPC Enfermedad de Parkinson."],
    [12,"Artritis idiopática juvenil/Artritis reumatoidea juvenil."],
    [13,"Esclerosis Multiple."],
    [14,"Diabetes Mellitus tipo 2."],
    [15,"Hipotiroidismo en personas de 15 años y más."],
    [16,"Hipertensión"],
    [17,"Glaoucoma"],
]

class FichaUsuario(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    nombre_tipo_usuario = models.ForeignKey(Tipo_usuario, on_delete=models.PROTECT)
    fecha_nacimiento = models.DateField()
    enfermades_cronicas = models.IntegerField(choices=enfermades_cronicas)

    def __str__ (self):
        return self.enfermades_cronicas




#-----------------------------------------------------------------------------------------------------------------#

#TABLA DE FAMILIAR
#class Familiar(models.Model):
#    id_familiar = models.AutoField(primary_key=True)
#    num_run_familiar = models.CharField(max_length=12)
#    nombre_familiar = models.CharField(max_length=100)
#    apellido_familiar = models.CharField(max_length=100)
#    email_familiar = models.EmailField()
#    telefono_familiar = models.IntegerField()
#    whatsapp_familiar = models.IntegerField()
#    celular_familiar = models.IntegerField()
#    telegram_familiar = models.IntegerField()
#    direccion_familiar = models.CharField(max_length=100)
#    id_comuna = models.ForeignKey(Comuna, on_delete=models.PROTECT)
#    id_region = models.ForeignKey(Region, on_delete=models.PROTECT)
#    id_provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT)
#    def __str__ (self):
#        return self.nombre_familiar

#-----------------------------------------------------------------------------------------------------------------#  

#OPCIONES DE CONSULTA EN CONTACTO
opciones_consulta = [
    [0,"Consulta"],
    [1,"Cotizacion"],
    [2,"Sugerencia"],
    [3,"Felicitaciones"],
    [4,"Reclamo"]
]

#CLASE DE CONTACTO
class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consulta)
    mensaje = models.TextField()
    def __str__(self):
        return self.nombre
#-----------------------------------------------------------------------------------------------------------------#




