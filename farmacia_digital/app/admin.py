from django.contrib import admin
from .models import Region, Provincia, Comuna, Laboratorio, Principio, ViaAdminstracion, Farmacia, FarmaciaSucursal, Medicamentos, MedicamentosDescuento, MedicamentoFichaTecnica, Tipo_usuario, Usuario, UsuarioReceta, UsuarioFarmacoVigilancia, Contacto, FichaUsuario

#ADMIN DE REGION
class RegionAdmin(admin.ModelAdmin):
    list_display = ("id_region","nombre_region")
    search_fields = ["nombre_region"]

#ADMIN DE PROVINCIA
class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ("id_provincia" ,"nombre_provincia")
    search_fields = ["nombre_provincia"]

#ADMIN DE COMUNA
class ComunaAdmin(admin.ModelAdmin):
    list_display = ("id_comuna","nombre_comuna")
    search_fields = ["nombre_comuna"]

#ADMIN DE LABORATORIO
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ("id_laboratorio","nombre_laboratorio")
    search_fields = ["nombre_laboratorio"]

#ADMIN DE PRINCIPIO ACTIVO
class PrincipioAdmin(admin.ModelAdmin):
    list_display = ("id_principio_activo","nombre_princio_activo")
    search_fields = ["nombre_princio_activo"]

#ADMIN DE VIA ADMINISTRACION
class ViaAdministracionAdmin(admin.ModelAdmin):
    list_display = ("id_via_administracion","nombre_via_administracion")
    search_fields = ["nombre_via_administracion"]

#ADMIN DE TIPO FARMACIA
class FarmaciaAdmin(admin.ModelAdmin):
    list_display = ("id_farmacia", "marca_farmacia")
    search_fields = ["marca_farmacia"]

#ADMIN DE TIPO FARMACIA SUCURSAL
class FarmaciaSucursalAdmin(admin.ModelAdmin):
    list_display = ("id_sucursal", "id_farmacia", "id_comuna", "id_region", "id_provincia", "direccion_sucursal", "telefono_sucursal", "email")
    search_fields = ["direccion_sucursal", "id_farmacia", "id_sucursal", "telefono_sucursal", "email"]

#ADMIN DE TIPO MEDICAMENTOS
class MedicamentosAdmin(admin.ModelAdmin):
    list_display = ("id_medicamento", "id_laboratorio", "id_principio_activo", "nombre_comercial",  "gramaje", "cantidad", "presentacion",  "lote", "id_via_administracion", "fecha_vencimento")
    search_fields = ["nombre_comercial", "id_medicamento", "id_laboratorio"]

class MedicamentosDescuentoAdmin(admin.ModelAdmin):
    list_display = ("id_descuento", "id_medicamento", "id_farmacia", "fecha_inicio_descuento",  "fecha_termino_descuento", "descuento_porcentaje")
    search_fields = ["id_descuento", "id_medicamento", "id_farmacia", "fecha_inicio_descuento",  "fecha_termino_descuento", "descuento_porcentaje"]

#ADMIN DE USUARIO
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id_usuario', 'id_tipo_usuario', 'num_run_usuario', 'nombres_usuario','apellido_paterno_usuario', 'appelido_materno_usuario', 'dirreccion_usuario', 'email_usuario', 'telefono_usuario')
    search_fields = ['id_usuario', 'id_tipo_usuario', 'num_run_usuario', 'nombres_usuario','apellido_paterno_usuario', 'appelido_materno_usuario', 'dirreccion_usuario', 'email_usuario', 'telefono_usuario']

#ADMIN DE MEDICAMENTO FICHA TECNICA
class MedicamentoFichaTecnicaAdmin(admin.ModelAdmin):
    list_display = ("id_ficha_medicamento", "nombre_comercial", "url_ficha")
    search_fields = ["id_ficha_medicamento", "nombre_comercial", "url_ficha"]

#ADMIN DE TIPO USUARIO
class Tipo_usuarioAdmin(admin.ModelAdmin):
    list_display = ("id_tipo_usuario", "nombre_tipo_usuario")
    search_fields = ["nombre_tipo_usuario"]

#ADMIN DE USUARIO RECETA
class UsuarioRecetaAdmin(admin.ModelAdmin):
    list_display = ('id_receta_usuario', 'fecha_registro', 'id_usuario', 'id_medicamento','tiempo_tratamiento', 'frecuencia_dosis', 'descripcion')
    search_fields = ['id_receta_usuario', 'fecha_registro', 'id_usuario', 'id_medicamento','tiempo_tratamiento', 'frecuencia_dosis', 'descripcion']

#ADMIN DE USUARIO FARMACO VIGILANGIA
class UsuarioFarmacoVigilanciaAdmin(admin.ModelAdmin):
    list_display  = ('id_farmaco', 'id_receta_usuario', 'horario_receta_1', 'horario_receta_2')
    search_fields = ['nombre', 'email', 'tipo_consulta', 'mensaje']

#ADMIN DE USUARIO FARMACO VIGILANGIA
class FichaUsuarioAdmin(admin.ModelAdmin):
    list_display  = ('id_usuario', 'nombre_tipo_usuario', 'fecha_nacimiento', 'enfermades_cronicas')
    search_fields = ['id_usuario', 'nombre_tipo_usuario', 'fecha_nacimiento', 'enfermades_cronicas']

#ADMIN DE CONTACTO
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'tipo_consulta', 'mensaje')
    search_fields = ['nombre', 'email', 'tipo_consulta', 'mensaje']

admin.site.register(Region, RegionAdmin)
admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Comuna, ComunaAdmin)
admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(Principio, PrincipioAdmin)
admin.site.register(ViaAdminstracion, ViaAdministracionAdmin)
admin.site.register(Farmacia, FarmaciaAdmin)
admin.site.register(FarmaciaSucursal, FarmaciaSucursalAdmin)
admin.site.register(Medicamentos, MedicamentosAdmin)
admin.site.register(MedicamentosDescuento, MedicamentosDescuentoAdmin)
admin.site.register(MedicamentoFichaTecnica, MedicamentoFichaTecnicaAdmin)
admin.site.register(Tipo_usuario, Tipo_usuarioAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(UsuarioReceta, UsuarioRecetaAdmin)
admin.site.register(UsuarioFarmacoVigilancia, UsuarioFarmacoVigilanciaAdmin)
admin.site.register(FichaUsuario, FichaUsuarioAdmin)
admin.site.register(Contacto, ContactoAdmin)
