import mysql.connector
import faker
from random import randint
Faker = faker.Faker()

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Tucontraseña",
    database="facturas2"
)

# Aqui hay parámetros para la configuración del poblado
# Se suele recomendar para poblar segun van haciendose pruebas
# Especialmente para validar consultas y rendimiento


cantidad_clientes = 200
cantidad_distribuidores = 30

facturas_maximas_por_cliente = 6
productos_maximos_por_distribuidor = 15

version = input("Ingrese la version de la base de datos (1 o 2): ")

cursor = conexion.cursor()

for i in range(cantidad_clientes):
    nombre_cliente = Faker.name()
    correo_cliente = Faker.email()
    cursor.execute(
    "INSERT INTO cliente (nombreCliente, correo) VALUES (%s,%s);",
    (nombre_cliente,correo_cliente)
)
    id_cliente = cursor.lastrowid  

    for j in range(randint(1,facturas_maximas_por_cliente)):
        fecha_emision = Faker.date_time_this_year()
        fecha_timestamp = fecha_emision.strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(
            "INSERT INTO factura (fechaHora, idCliente) VALUES (%s,%s);",
            (fecha_timestamp, id_cliente)
        )



for i in range(cantidad_distribuidores):
    if version == '1':
        nombre_distribuidor = Faker.company()
        
        cursor.execute(
            "INSERT INTO distribuidor (nombreDistribuidor) VALUES (%s);",
            (nombre_distribuidor,)
        )

        idDistribuidor = cursor.lastrowid
    elif version == '2':
        nombre_distribuidor = Faker.company()
        idPais = randint(1,10)
        
        cursor.execute(
            "INSERT INTO distribuidor (nombreDistribuidor, idPais) VALUES (%s, %s);",
            (nombre_distribuidor,idPais)
        )

        idDistribuidor = cursor.lastrowid

    for p in range(randint(1,productos_maximos_por_distribuidor)):
        if version == '1':
            nombre_producto = Faker.word().capitalize()
            precio_producto = randint(100,10000)
            cursor.execute(
                "INSERT INTO producto (nombreProducto, precio, idDistribuidor) VALUES (%s, %s,%s);",
                (nombre_producto, precio_producto,idDistribuidor)
            )
        elif version == '2':
            nombre_producto = Faker.word().capitalize()
            precio_producto = randint(100,10000)
            limit = 5
            idTipoProducto = randint(1,limit)
            cursor.execute(
                "INSERT INTO producto (nombreProducto, precio, idDistribuidor, idTipoProducto) VALUES (%s, %s,%s, %s);",
                (nombre_producto, precio_producto,idDistribuidor, idTipoProducto)
            )
    
conexion.commit()
cursor.close()
conexion.close()
