import mysql.connector
import faker
from random import randint
Faker = faker.Faker()

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="TuContraseña",
    database="facturas"
)

# Aqui hay parámetros para la configuración del poblado
# Se suele recomendar para poblar segun van haciendose pruebas
# Especialmente para validar consultas y rendimiento


cantidad_clientes = 200
cantidad_distribuidores = 15

facturas_maximas_por_cliente = 4
productos_maximos_por_distribuidor = 10



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
            "INSERT INTO factura (fecha, idCliente) VALUES (%s,%s);",
            (fecha_timestamp, id_cliente)
        )



for i in range(cantidad_distribuidores):
    nombre_distribuidor = Faker.company()
    
    cursor.execute(
        "INSERT INTO distribuidor (nombreDistribuidor) VALUES (%s);",
        (nombre_distribuidor,)
    )

    idDistribuidor = cursor.lastrowid

    for p in range(randint(1,productos_maximos_por_distribuidor)):
        nombre_producto = Faker.word().capitalize()
        precio_producto = randint(100,10000)
        cursor.execute(
            "INSERT INTO producto (nombreProducto, precio, idDistribuidor) VALUES (%s, %s,%s);",
            (nombre_producto, precio_producto,idDistribuidor)
        )
    
conexion.commit()
cursor.close()
conexion.close()
