from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Cliente, Mujer, Hombre, Ninas, Ninos, Pedido, Reseña
from django.utils import timezone

# ==========================================
# VISTAS PRINCIPALES
# ==========================================
def inicio_famfashion(request):
    return render(request, 'app_famfashion/inicio.html')
# ==========================================
# VISTAS PARA CLIENTES
# ==========================================
def agregar_cliente(request):
    if request.method == 'POST':
        cliente = Cliente(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            email=request.POST['email'],
            telefono=request.POST['telefono'],
            contraseña=request.POST['contraseña'],
            calle=request.POST['calle'],
            numero_casa=request.POST['numero_casa'],
            colonia=request.POST['colonia'],
            ciudad=request.POST['ciudad'],
            codigo_postal=request.POST['codigo_postal'],
            descripcion_direccion=request.POST['descripcion_direccion'],
            metodo_pago=request.POST['metodo_pago']
        )
        cliente.save()
        return redirect('ver_clientes')
    return render(request, 'app_famfashion/clientes/agregar_cliente.html')

def ver_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'app_famfashion/clientes/ver_clientes.html', {'clientes': clientes})

def actualizar_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    if request.method == 'POST':
        cliente.nombre = request.POST['nombre']
        cliente.apellido = request.POST['apellido']
        cliente.email = request.POST['email']
        cliente.telefono = request.POST['telefono']
        cliente.contraseña = request.POST['contraseña']
        cliente.calle = request.POST['calle']
        cliente.numero_casa = request.POST['numero_casa']
        cliente.colonia = request.POST['colonia']
        cliente.ciudad = request.POST['ciudad']
        cliente.codigo_postal = request.POST['codigo_postal']
        cliente.descripcion_direccion = request.POST['descripcion_direccion']
        cliente.metodo_pago = request.POST['metodo_pago']
        cliente.save()
        return redirect('ver_clientes')
    return render(request, 'app_famfashion/clientes/actualizar_cliente.html', {'cliente': cliente})

def borrar_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_clientes')
    return render(request, 'app_famfashion/clientes/borrar_cliente.html', {'cliente': cliente})

# ==========================================
# VISTAS PARA PRODUCTOS MUJER
# ==========================================
def agregar_mujer(request):
    if request.method == 'POST':
        mujer = Mujer(
            nombre_producto=request.POST['nombre_producto'],
            descripcion=request.POST['descripcion'],
            talla=request.POST['talla'],
            color=request.POST['color'],
            precio=request.POST['precio'],
            stock=request.POST['stock'],
            material=request.POST['material'],
            temporada=request.POST['temporada'],
            tipo=request.POST['tipo']
        )
        if 'imagen' in request.FILES:
            mujer.imagen = request.FILES['imagen']
        mujer.save()
        return redirect('ver_mujer')
    return render(request, 'app_famfashion/productos/mujer/agregar_mujer.html')

def ver_mujer(request):
    productos = Mujer.objects.all()
    return render(request, 'app_famfashion/productos/mujer/ver_mujer.html', {'productos': productos})

def actualizar_mujer(request, id_producto):
    producto = get_object_or_404(Mujer, id_producto=id_producto)
    if request.method == 'POST':
        producto.nombre_producto = request.POST['nombre_producto']
        producto.descripcion = request.POST['descripcion']
        producto.talla = request.POST['talla']
        producto.color = request.POST['color']
        producto.precio = request.POST['precio']
        producto.stock = request.POST['stock']
        producto.material = request.POST['material']
        producto.temporada = request.POST['temporada']
        producto.tipo = request.POST['tipo']
        if 'imagen' in request.FILES:
            producto.imagen = request.FILES['imagen']
        producto.save()
        return redirect('ver_mujer')
    return render(request, 'app_famfashion/productos/mujer/actualizar_mujer.html', {'producto': producto})

def borrar_mujer(request, id_producto):
    producto = get_object_or_404(Mujer, id_producto=id_producto)
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_mujer')
    return render(request, 'app_famfashion/productos/mujer/borrar_mujer.html', {'producto': producto})

# ==========================================
# VISTAS PARA PRODUCTOS HOMBRE
# ==========================================
def agregar_hombre(request):
    if request.method == 'POST':
        hombre = Hombre(
            nombre_producto=request.POST['nombre_producto'],
            descripcion=request.POST['descripcion'],
            talla=request.POST['talla'],
            color=request.POST['color'],
            precio=request.POST['precio'],
            stock=request.POST['stock'],
            material=request.POST['material'],
            temporada=request.POST['temporada'],
            tipo=request.POST['tipo']
        )
        if 'imagen' in request.FILES:
            hombre.imagen = request.FILES['imagen']
        hombre.save()
        return redirect('ver_hombre')
    return render(request, 'app_famfashion/productos/hombre/agregar_hombre.html')

def ver_hombre(request):
    productos = Hombre.objects.all()
    return render(request, 'app_famfashion/productos/hombre/ver_hombre.html', {'productos': productos})

def actualizar_hombre(request, id_producto):
    producto = get_object_or_404(Hombre, id_producto=id_producto)
    if request.method == 'POST':
        producto.nombre_producto = request.POST['nombre_producto']
        producto.descripcion = request.POST['descripcion']
        producto.talla = request.POST['talla']
        producto.color = request.POST['color']
        producto.precio = request.POST['precio']
        producto.stock = request.POST['stock']
        producto.material = request.POST['material']
        producto.temporada = request.POST['temporada']
        producto.tipo = request.POST['tipo']
        if 'imagen' in request.FILES:
            producto.imagen = request.FILES['imagen']
        producto.save()
        return redirect('ver_hombre')
    return render(request, 'app_famfashion/productos/hombre/actualizar_hombre.html', {'producto': producto})

def borrar_hombre(request, id_producto):
    producto = get_object_or_404(Hombre, id_producto=id_producto)
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_hombre')
    return render(request, 'app_famfashion/productos/hombre/borrar_hombre.html', {'producto': producto})

# ==========================================
# VISTAS PARA PEDIDOS
# ==========================================
def ver_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'app_famfashion/pedidos/ver_pedidos.html', {'pedidos': pedidos})

def detalle_pedido(request, id_pedido):
    pedido = get_object_or_404(Pedido, id_pedido=id_pedido)
    return render(request, 'app_famfashion/pedidos/detalle_pedido.html', {'pedido': pedido})

def actualizar_estado_pedido(request, id_pedido):
    pedido = get_object_or_404(Pedido, id_pedido=id_pedido)
    if request.method == 'POST':
        pedido.estado = request.POST['estado']
        pedido.save()
        return redirect('ver_pedidos')
    return render(request, 'app_famfashion/pedidos/actualizar_estado_pedido.html', {'pedido': pedido})

# ==========================================
# VISTAS PARA RESEÑAS
# ==========================================
def ver_resenas(request):
    resenas = Reseña.objects.all()
    return render(request, 'app_famfashion/resenas/ver_resenas.html', {'resenas': resenas})

def agregar_resena(request):
    if request.method == 'POST':
        try:
            # Obtener el primer cliente disponible o crear una reseña sin cliente
            cliente = Cliente.objects.first()  # O puedes hacer un select para que el usuario elija
            
            resena = Reseña(
                id_cliente=cliente,  # Asignar un cliente
                calificacion=request.POST['calificacion'],
                comentario=request.POST['comentario']
            )
            if 'foto_producto' in request.FILES:
                resena.foto_producto = request.FILES['foto_producto']
            resena.save()
            return redirect('ver_resenas')
        except Exception as e:
            print(f"Error al crear reseña: {e}")
            # Manejar el error apropiadamente
    
    # Pasar clientes al template para selección
    clientes = Cliente.objects.all()
    return render(request, 'app_famfashion/resenas/agregar_resena.html', {'clientes': clientes})
def borrar_resena(request, id_reseña):
    resena = get_object_or_404(Reseña, id_reseña=id_reseña)
    if request.method == 'POST':
        resena.delete()
        return redirect('ver_resenas')
    return render(request, 'app_famfashion/resenas/borrar_resena.html', {'resena': resena})

# ==========================================
# VISTAS PARA PRODUCTOS NIÑAS
# ==========================================
def agregar_ninas(request):
    if request.method == 'POST':
        ninas = Ninas(
            nombre_producto=request.POST['nombre_producto'],
            descripcion=request.POST['descripcion'],
            talla=request.POST['talla'],
            color=request.POST['color'],
            precio=request.POST['precio'],
            stock=request.POST['stock'],
            material=request.POST['material'],
            temporada=request.POST['temporada'],
            tipo=request.POST['tipo'],
            edad_recomendada=request.POST['edad_recomendada']
        )
        if 'imagen' in request.FILES:
            ninas.imagen = request.FILES['imagen']
        ninas.save()
        return redirect('ver_ninas')
    return render(request, 'app_famfashion/productos/ninas/agregar_ninas.html')

def ver_ninas(request):
    productos = Ninas.objects.all()
    return render(request, 'app_famfashion/productos/ninas/ver_ninas.html', {'productos': productos})

def actualizar_ninas(request, id_producto):
    producto = get_object_or_404(Ninas, id_producto=id_producto)
    if request.method == 'POST':
        producto.nombre_producto = request.POST['nombre_producto']
        producto.descripcion = request.POST['descripcion']
        producto.talla = request.POST['talla']
        producto.color = request.POST['color']
        producto.precio = request.POST['precio']
        producto.stock = request.POST['stock']
        producto.material = request.POST['material']
        producto.temporada = request.POST['temporada']
        producto.tipo = request.POST['tipo']
        producto.edad_recomendada = request.POST['edad_recomendada']
        if 'imagen' in request.FILES:
            producto.imagen = request.FILES['imagen']
        producto.save()
        return redirect('ver_ninas')
    return render(request, 'app_famfashion/productos/ninas/actualizar_ninas.html', {'producto': producto})

def borrar_ninas(request, id_producto):
    producto = get_object_or_404(Ninas, id_producto=id_producto)
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_ninas')
    return render(request, 'app_famfashion/productos/ninas/borrar_ninas.html', {'producto': producto})

# ==========================================
# VISTAS PARA PRODUCTOS NIÑOS
# ==========================================
def agregar_ninos(request):
    if request.method == 'POST':
        ninos = Ninos(
            nombre_producto=request.POST['nombre_producto'],
            descripcion=request.POST['descripcion'],
            talla=request.POST['talla'],
            color=request.POST['color'],
            precio=request.POST['precio'],
            stock=request.POST['stock'],
            material=request.POST['material'],
            temporada=request.POST['temporada'],
            tipo=request.POST['tipo'],
            edad_recomendada=request.POST['edad_recomendada']
        )
        if 'imagen' in request.FILES:
            ninos.imagen = request.FILES['imagen']
        ninos.save()
        return redirect('ver_ninos')
    return render(request, 'app_famfashion/productos/ninos/agregar_ninos.html')

def ver_ninos(request):
    productos = Ninos.objects.all()
    return render(request, 'app_famfashion/productos/ninos/ver_ninos.html', {'productos': productos})

def actualizar_ninos(request, id_producto):
    producto = get_object_or_404(Ninos, id_producto=id_producto)
    if request.method == 'POST':
        producto.nombre_producto = request.POST['nombre_producto']
        producto.descripcion = request.POST['descripcion']
        producto.talla = request.POST['talla']
        producto.color = request.POST['color']
        producto.precio = request.POST['precio']
        producto.stock = request.POST['stock']
        producto.material = request.POST['material']
        producto.temporada = request.POST['temporada']
        producto.tipo = request.POST['tipo']
        producto.edad_recomendada = request.POST['edad_recomendada']
        if 'imagen' in request.FILES:
            producto.imagen = request.FILES['imagen']
        producto.save()
        return redirect('ver_ninos')
    return render(request, 'app_famfashion/productos/ninos/actualizar_ninos.html', {'producto': producto})

def borrar_ninos(request, id_producto):
    producto = get_object_or_404(Ninos, id_producto=id_producto)
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_ninos')
    return render(request, 'app_famfashion/productos/ninos/borrar_ninos.html', {'producto': producto})

# ==========================================
# VISTA PARA BORRAR PEDIDO
# ==========================================
def borrar_pedido(request, id_pedido):
    pedido = get_object_or_404(Pedido, id_pedido=id_pedido)
    if request.method == 'POST':
        pedido.delete()
        return redirect('ver_pedidos')
    return render(request, 'app_famfashion/pedidos/borrar_pedido.html', {'pedido': pedido})
def agregar_pedido(request):
    if request.method == 'POST':
        # Obtener el cliente
        cliente_id = request.POST.get('id_cliente')
        cliente = None
        if cliente_id:
            cliente = Cliente.objects.get(id_cliente=cliente_id)
        
        # Calcular total
        cantidad = int(request.POST['cantidad'])
        precio_unitario = float(request.POST['precio_unitario'])
        total = cantidad * precio_unitario
        
        pedido = Pedido(
            id_cliente=cliente,
            nombre_producto=request.POST['nombre_producto'],
            cantidad=cantidad,
            precio_unitario=precio_unitario,
            total=total,
            metodo_pago=request.POST['metodo_pago'],
            estado=request.POST['estado'],
            direccion=request.POST['direccion']
        )
        pedido.save()
        return redirect('ver_pedidos')
    
    # Obtener datos para el formulario
    clientes = Cliente.objects.all()
    productos_mujer = Mujer.objects.all()
    productos_hombre = Hombre.objects.all()
    productos_ninas = Ninas.objects.all()
    productos_ninos = Ninos.objects.all()
    
    context = {
        'clientes': clientes,
        'productos_mujer': productos_mujer,
        'productos_hombre': productos_hombre,
        'productos_ninas': productos_ninas,
        'productos_ninos': productos_ninos,
    }
    return render(request, 'app_famfashion/pedidos/agregar_pedido.html', context)


# ==========================================
# VISTA PARA ACTUALIZAR RESEÑA
# ==========================================
def ver_resenas(request):
    try:
        resenas = Reseña.objects.all()
        # Verificar que todas las reseñas tengan id válido
        for resena in resenas:
            print(f"Reseña ID: {resena.id_reseña}, Cliente: {resena.id_cliente}")
    except Exception as e:
        print(f"Error al cargar reseñas: {e}")
        resenas = []
    
    return render(request, 'app_famfashion/resenas/ver_resenas.html', {'resenas': resenas})

def actualizar_resena(request, id_reseña):  # Asegúrate de que el parámetro sea id_reseña
    resena = get_object_or_404(Reseña, id_reseña=id_reseña)
    if request.method == 'POST':
        resena.calificacion = request.POST['calificacion']
        resena.comentario = request.POST['comentario']
        if 'foto_producto' in request.FILES:
            resena.foto_producto = request.FILES['foto_producto']
        resena.save()
        return redirect('ver_resenas')
    
    clientes = Cliente.objects.all()
    return render(request, 'app_famfashion/resenas/actualizar_resena.html', {
        'resena': resena,
        'clientes': clientes
    })