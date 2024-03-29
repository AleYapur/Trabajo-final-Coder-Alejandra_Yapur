Proyecto final: Aplicación de ventas en línea

Autora: Alejandra Yapur
Fecha: 29/03/24
Versión: 1.0

Objetivo: Crear un sitio web usando Django

Consideraciones:

Clonar este repositorio en tu máquina local usando GitBash.
Ejecutar: python -m pip install Pillow 
En la terminal, ejecutar el servidor con el comando: python manage.py runserver.
Abrir un navegador y ejecutar http://127.0.0.1:8000/ para ver la página principal.
Para ver todos los productos en stock, ir a Tienda>Todos los productos.
Para buscar una planta en particular, ir a Tienda>Buscar.
Para agregar un nuevo producto, en la barra de navegación ir a Interno>Nuevo producto.
Para agregar un nuevo producto, en la barra de navegación ir a Interno>Nuevo cliente.
Para acceder a la vista de administrador, ir a http://127.0.0.1:8000/admin e ingresar los datos siguientes:
    Usuario: admin01 
    Contraseña 200380773mj%

Modelos usados:
- Producto: los artículos principales que venden en la tienda
- Cliente: clientes almacenados en la base de datos
- Avatar: relacionado con el perfil de cada usuario
- Orden: pedidos que los clientes realizan en el sitio

Pruebas:
1. Iniciar sesión:	Inicia sesión, aparecen opciones adicionales y el nombre de usuario en la barra de navegación
2. Cambiar el avatar:	Click en la imagen de perfil, direcciona a la página para cambiar avatar, selección de archivo, actualización de avatar, nueva imagen de avatar aparece al lado del nombre de perfil en la barra de navegación
3. Cerrar sesión:	Cierra sesión, dirige a la página de cierre de sesión con el mensaje correspondiente. Desaparecen las opciones adicionales de la barra de navegación y aparecen los botones Loguearse y Resgistrarse
4. Registrarse:	Hacer clic en el botón registrarse, dirige al formulario correspondiente. Crea usuario
5. Crear una orden:	Ir a Ordenes, hacer clic en el +, dirige al formulario de ordenes, completarlo y que se agregue a la base de datos
6. Eliminar una orden:	Hacer clic en una orden ya creada y comprobar que desaparezca de la base de datos
7. Agregar un cliente:	Ir a Clientes, hacer clic en el +, dirige al formulario de clientes, completarlo y que se agregue a la base de datos


Video con la presentación del sitio: https://www.loom.com/share/a91ca01be0ee4f349d22fca418fbfa2d?sid=66deebfa-899c-4bec-b5d4-fe6540f1c377

