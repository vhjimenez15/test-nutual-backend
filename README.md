# Prueba técnica (flask-application)
## Antecedentes
En los últimos años, en la industria de Real Estate se han popularizado los sistemas de
valoración automática (AVM) basados en modelos de Machine Learning. En el caso más
simple, puede ser un modelo de regresión lineal o puede ser un conjunto de modelos
empleando KNN, Random Forest, Gradient Boosting, etc.

Supongamos que existe ya un modelo de Machine Learning como el descrito anteriormente
funcionando como un API (AVM-API) que hace una predicción del precio de venta de un
apartamento empleando múltiples fuentes de datos.
Descripción del problema
Adjunto puedes encontrar un fichero con una descripción del formato de la salida del API del
AVM (API-AVM).
El problema consiste en:
- Crear una aplicación basada en APIs que lea la salida del AVM, actualice una base
de datos con el resultado, y muestre el resultado en el frontend.
- Exponer un API para obtener información agregada del valor medio del metro
cuadrado en una determinada ciudad o área de la ciudad.

### Fichero (data ejemplo)
```
[
   {
      "address":"Carrer de Pau Alsina 10, Principal A",
      "latitude":41.410610,
      "longitude":2.161880,
      "zipcode":"08025",
      "city":"Barcelona",
      "year_of_construction":1900,
      "year_of_renovation":2020,
      "total_price":450000,
      "total_area":83,
      "price_m2":5421,
      "has_elevator":"Y",
      "“valuation_date":"10/09/2021"
   }
]
```

## Implementación
Se creó una aplicación backend construida en flask (framework para python), SQLAlchemy (Como ORM) y MYSql (la base de datos). Esta cuenta con dos apps principales user y AWV, la primera para usuarios y authenticación, y la segunda para "valoración automática" (AVM). Las cuales se encuentran separadas entendiendo la separación de responsabilidad (SOLID).

# Pasos para correr la aplicacion en local (Backend)

Descargue el archivo o clone el repositorio en la respectiva máquina de prueba ("agregar repositorio").

Si tiene git y desea clonarlo del repositorio ejecute:
```
git clone "agregar repositorio"
```
Entre a la carpeta test-nutual-backend, abra una terminal de su preferencia y ejecute:
```
docker-compose up --build
```

> [!NOTE]
> Tenga en cuenta que debe tener instalado docker para esta implementación (https://docs.docker.com/engine/install/).

Cuando la el contenedor de docker haya lanzado de manera exitosa a la aplicación del backend se habilitará el puerto 5000 del localhost para poder hacer uso de la misma.

Luego ejecuto los siguientes comandos para dejar operativo el backend:
```
docker exec -it nutual_server_flask bash
```
Dentro del contenedor ejecute:
```
flask db init
flask db migrate -m "<migration_name>"
flask db upgrade
```
Luego:
```
flask initial_command
```
Para crear el usuario con que se realizaran las pruebas debe ejecutar el comando:
```
flask create_user username password
```
Donde ***username*** y ***password*** son el usuario y la contraseña respectivamente.

Despues de esto el backend estará listo para ser probado desde postman

## APIs en postman
Se creó un collection en postman el cual puede exportar con (https://api.postman.com/collections/17659172-726e55e8-a600-4930-8c7b-895630fb89a7?access_key=PMAT-01HMNVDF07R3ZVGBAG7RMQ98A6).

Para poder hacer uso del collection en postman es necesario agregar http://localhost:5173/ al valor de la variable host ({{host}}) en la carpeta principal del collectión (Donde dice "Variables"), aunque es posible que ya se encuentre agregada.

> [!TIP]
> Recuerde hacer login antes de usar cualquier endponit o se le denegará la autenticación.

### Paso siguiente
Desplegar la aplicación del front.
