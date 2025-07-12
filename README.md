# PYTHON + DJANGO + POSTGRES

## Implementación

__Utilización de consola__ 

```s
# Creación de un entorno virtual
# Instalación de dependencias

pip install django==5.0 psycopg2

# Creación del proyecto usando Django

django-admin startproject sistema_venta

# Cambiamos a la carpeta del proyecto creado
cd .\sistema_venta

# Creación del CORE de la aplicación
python manage.py startapp core

# Creación del archivo url.py en core

New-Item core\url.py

```

- En sistema_venta > setting.py
  - Agregar la carpeta CORE dentro de INSTALLED_APPS
  - Modificar la conexión a Postgres en DATABASES
- En CORE > models.py
  - Creación de los modelos que serán las tablas en POSTGRES

__Utilización de consola__ 

```s
# Definir la estructura de los models
python manage.py makemigrations core

# Hacer las migraciones de los models
python manage.py migrate

# Crear un superusuario para gestionar los registros por Django
python manage.py createsuperuser
## Agregan sus credenciales

# Corremos el servidor de Django
python manage.py runserver
## usamos las credenciales del superusuario creado anteriormente

```

> Nota: Para visualizar `los datos ordenados` en el servidor de Django, se `agrega la clase Meta` en una de las clases creadas en `models.py` indicando el campo en que se ordenará. Si quieren ordenar descendente, solo agregar un `-` seguido del nombre del campo.

## Conexión a Postgres mediante la Shell

- Se tiene que estar dentro de la carpeta creada cuando usamos `django-admin`
```s
# Conectamos a la Shell de Django
python manage.py shell

# Indicamos qué modelo se usará 
from core.models import Producto

# Asignamos en una variable todos los datos
productos = Producto.objects.all()

# Recorremos la variable para mostrar los datos
for producto in productos:
    print(producto.nombre, producto.precio)
## Doble enter para mostrar los datos

# Obtener un solo dato
producto_unico = Producto.objects.get(id=1)
print(producto_unico.nombre, producto_unico.precio)

# Filtrar datos cuyos productos menores a 10
productos_baratos = Producto.objects.filter(precio__lt=100.00)
for producto in productos_baratos:
    print(producto.nombre, producto.precio)

# Crear un nuevo datos
from core.models import Cliente
cliente = Cliente(nombre='Juan', email='juanp@gmail.com', telefono='1234560', direccion='ate 123')
cliente.save()
## Doble enter para guardar los datos

# Eliminar un dato
cliente = Cliente.objects.get(id=1)
cliente.delete()

# Modificar un dato
cliente = Cliente.objects.get(id=3)
cliente.direccion = 'Av Los Jazmines'
cliente.save()

# Salir de la shell
exit()
```