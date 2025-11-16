from django.db import models
from django.utils import timezone

# ==========================================
# MODELO: MUJER
# ==========================================
class Mujer(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    talla = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    material = models.CharField(max_length=100, blank=True)
    imagen = models.ImageField(upload_to='productos/mujer/', blank=True, null=True)
    temporada = models.CharField(max_length=20, choices=[('verano','Verano'),('invierno','Invierno')])
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre_producto} ({self.tipo})"

# ==========================================
# MODELO: HOMBRE
# ==========================================
class Hombre(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    talla = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    material = models.CharField(max_length=100, blank=True)
    imagen = models.ImageField(upload_to='productos/hombre/', blank=True, null=True)
    tipo = models.CharField(max_length=100)
    temporada = models.CharField(max_length=20, choices=[('verano','Verano'),('invierno','Invierno')])

    def __str__(self):
        return f"{self.nombre_producto} ({self.tipo})"

# ==========================================
# MODELO: NIÑAS
# ==========================================
class Ninas(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=200)
    tipo = models.CharField(max_length=100)
    talla = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    descripcion = models.TextField(blank=True)
    material = models.CharField(max_length=100, blank=True)
    temporada = models.CharField(max_length=20, choices=[('verano','Verano'),('invierno','Invierno')])
    edad_recomendada = models.CharField(max_length=50, blank=True)
    imagen = models.ImageField(upload_to='productos/ninas/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_producto} ({self.tipo})"

# ==========================================
# MODELO: NIÑOS
# ==========================================
class Ninos(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=200)
    tipo = models.CharField(max_length=100)
    talla = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    descripcion = models.TextField(blank=True)
    material = models.CharField(max_length=100, blank=True)
    temporada = models.CharField(max_length=20, choices=[('verano','Verano'),('invierno','Invierno')])
    edad_recomendada = models.CharField(max_length=50, blank=True)
    imagen = models.ImageField(upload_to='productos/ninos/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_producto} ({self.tipo})"

# ==========================================
# MODELO: CLIENTE
# ==========================================
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=50, blank=True)
    contraseña = models.CharField(max_length=128)
    calle = models.CharField(max_length=200, blank=True)
    numero_casa = models.CharField(max_length=50, blank=True)
    colonia = models.CharField(max_length=100, blank=True)
    ciudad = models.CharField(max_length=100, blank=True)
    codigo_postal = models.CharField(max_length=20, blank=True)
    descripcion_direccion = models.TextField(blank=True)
    fecha_registro = models.DateTimeField(default=timezone.now)
    metodo_pago = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# ==========================================
# MODELO: PEDIDO
# ==========================================
class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, db_column='id_cliente', related_name='pedidos')
    id_producto_mujer = models.ForeignKey(Mujer, on_delete=models.SET_NULL, null=True, blank=True)
    id_producto_hombre = models.ForeignKey(Hombre, on_delete=models.SET_NULL, null=True, blank=True)
    id_producto_ninas = models.ForeignKey(Ninas, on_delete=models.SET_NULL, null=True, blank=True)
    id_producto_ninos = models.ForeignKey(Ninos, on_delete=models.SET_NULL, null=True, blank=True)
    nombre_producto = models.CharField(max_length=200)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=12, decimal_places=2)
    fecha_pedido = models.DateTimeField(default=timezone.now)
    metodo_pago = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    direccion = models.TextField(blank=True)

    def __str__(self):
        return f"Pedido {self.id_pedido} - {self.nombre_producto} x{self.cantidad}"

# ==========================================
# MODELO: RESEÑA
# ==========================================
class Reseña(models.Model):
    id_reseña = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, db_column='id_cliente', related_name='reseñas')
    id_producto_mujer = models.ForeignKey(Mujer, on_delete=models.SET_NULL, null=True, blank=True)
    id_producto_hombre = models.ForeignKey(Hombre, on_delete=models.SET_NULL, null=True, blank=True)
    id_producto_ninas = models.ForeignKey(Ninas, on_delete=models.SET_NULL, null=True, blank=True)
    id_producto_ninos = models.ForeignKey(Ninos, on_delete=models.SET_NULL, null=True, blank=True)
    calificacion = models.PositiveSmallIntegerField()
    comentario = models.TextField(blank=True)
    fecha = models.DateTimeField(default=timezone.now)
    foto_producto = models.ImageField(upload_to='reseñas/', blank=True, null=True)

    def __str__(self):
        return f"Reseña {self.id_reseña} - {self.calificacion} estrellas"