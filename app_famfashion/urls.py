from django.urls import path
from . import views

urlpatterns = [
    # Página principal
    path('', views.inicio_famfashion, name='inicio_famfashion'),
    
    # URLs para Clientes
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/ver/', views.ver_clientes, name='ver_clientes'),
    path('clientes/actualizar/<int:id_cliente>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('clientes/borrar/<int:id_cliente>/', views.borrar_cliente, name='borrar_cliente'),
    
    # URLs para Productos Mujer
    path('mujer/agregar/', views.agregar_mujer, name='agregar_mujer'),
    path('mujer/ver/', views.ver_mujer, name='ver_mujer'),
    path('mujer/actualizar/<int:id_producto>/', views.actualizar_mujer, name='actualizar_mujer'),
    path('mujer/borrar/<int:id_producto>/', views.borrar_mujer, name='borrar_mujer'),
    
    # URLs para Productos Hombre
    path('hombre/agregar/', views.agregar_hombre, name='agregar_hombre'),
    path('hombre/ver/', views.ver_hombre, name='ver_hombre'),
    path('hombre/actualizar/<int:id_producto>/', views.actualizar_hombre, name='actualizar_hombre'),
    path('hombre/borrar/<int:id_producto>/', views.borrar_hombre, name='borrar_hombre'),
    
    # URLs para Productos Niñas
    path('ninas/agregar/', views.agregar_ninas, name='agregar_ninas'),
    path('ninas/ver/', views.ver_ninas, name='ver_ninas'),
    path('ninas/actualizar/<int:id_producto>/', views.actualizar_ninas, name='actualizar_ninas'),
    path('ninas/borrar/<int:id_producto>/', views.borrar_ninas, name='borrar_ninas'),
    
    # URLs para Productos Niños
    path('ninos/agregar/', views.agregar_ninos, name='agregar_ninos'),
    path('ninos/ver/', views.ver_ninos, name='ver_ninos'),
    path('ninos/actualizar/<int:id_producto>/', views.actualizar_ninos, name='actualizar_ninos'),
    path('ninos/borrar/<int:id_producto>/', views.borrar_ninos, name='borrar_ninos'),
    
    # URLs para Pedidos
    path('pedidos/ver/', views.ver_pedidos, name='ver_pedidos'),
    path('pedidos/detalle/<int:id_pedido>/', views.detalle_pedido, name='detalle_pedido'),
    path('pedidos/actualizar/<int:id_pedido>/', views.actualizar_estado_pedido, name='actualizar_estado_pedido'),
    path('pedidos/borrar/<int:id_pedido>/', views.borrar_pedido, name='borrar_pedido'),
    # Agregar esta línea en las URLs de pedidos
    path('pedidos/agregar/', views.agregar_pedido, name='agregar_pedido'),
 # URLs para Reseñas
    path('resenas/ver/', views.ver_resenas, name='ver_resenas'),
    path('resenas/agregar/', views.agregar_resena, name='agregar_resena'),
    path('resenas/actualizar/<int:id_reseña>/', views.actualizar_resena, name='actualizar_resena'),  # CAMBIAR id_resena por id_reseña
    path('resenas/borrar/<int:id_reseña>/', views.borrar_resena, name='borrar_resena'),  # CAMBIAR id_resena por id_reseña
]