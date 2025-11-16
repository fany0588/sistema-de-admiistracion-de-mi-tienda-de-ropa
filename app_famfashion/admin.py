from django.contrib import admin
from .models import Cliente, Mujer, Hombre, Ninas, Ninos, Pedido, Reseña

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id_cliente', 'nombre', 'apellido', 'email', 'ciudad', 'fecha_registro')
    search_fields = ('nombre', 'apellido', 'email')

@admin.register(Mujer)
class MujerAdmin(admin.ModelAdmin):
    list_display = ('id_producto', 'nombre_producto', 'tipo', 'talla', 'precio', 'stock')
    list_filter = ('tipo', 'temporada')

@admin.register(Hombre)
class HombreAdmin(admin.ModelAdmin):
    list_display = ('id_producto', 'nombre_producto', 'tipo', 'talla', 'precio', 'stock')
    list_filter = ('tipo', 'temporada')

@admin.register(Ninas)
class NinasAdmin(admin.ModelAdmin):
    list_display = ('id_producto', 'nombre_producto', 'tipo', 'talla', 'precio', 'edad_recomendada')
    list_filter = ('tipo', 'temporada')

@admin.register(Ninos)
class NinosAdmin(admin.ModelAdmin):
    list_display = ('id_producto', 'nombre_producto', 'tipo', 'talla', 'precio', 'edad_recomendada')
    list_filter = ('tipo', 'temporada')

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id_pedido', 'id_cliente', 'nombre_producto', 'cantidad', 'total', 'estado')
    list_filter = ('estado', 'fecha_pedido')

@admin.register(Reseña)
class ReseñaAdmin(admin.ModelAdmin):
    list_display = ('id_reseña', 'id_cliente', 'calificacion', 'fecha')
    list_filter = ('calificacion', 'fecha')