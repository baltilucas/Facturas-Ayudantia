import mysql from "mysql2/promise";
import { faker } from "@faker-js/faker";

// Configuración de conexión
const conexion = await mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "TuContraseña",
  database: "facturas",
});

// Parámetros de configuración del poblado
const cantidad_clientes = 200;
const cantidad_distribuidores = 15;

const facturas_maximas_por_cliente = 4;
const productos_maximos_por_distribuidor = 10;

try {
  console.log("Conectado a la base de datos");

  // Poblar clientes y facturas
  for (let i = 0; i < cantidad_clientes; i++) {
    const nombre_cliente = faker.person.fullName();
    const correo_cliente = faker.internet.email();

    const [clienteResult] = await conexion.execute(
      "INSERT INTO cliente (nombreCliente, correo) VALUES (?, ?);",
      [nombre_cliente, correo_cliente]
    );

    const id_cliente = clienteResult.insertId;

    const cantidad_facturas = faker.number.int({
      min: 1,
      max: facturas_maximas_por_cliente,
    });
    for (let j = 0; j < cantidad_facturas; j++) {
      const fecha_emision = faker.date.recent({ days: 365 });
      const fecha_timestamp = fecha_emision
        .toISOString()
        .slice(0, 19)
        .replace("T", " ");

      await conexion.execute(
        "INSERT INTO factura (fecha, idCliente) VALUES (?, ?);",
        [fecha_timestamp, id_cliente]
      );
    }
  }

  // Poblar distribuidores y productos
  for (let i = 0; i < cantidad_distribuidores; i++) {
    const nombre_distribuidor = faker.company.name();

    const [distribuidorResult] = await conexion.execute(
      "INSERT INTO distribuidor (nombreDistribuidor) VALUES (?);",
      [nombre_distribuidor]
    );

    const idDistribuidor = distribuidorResult.insertId;

    const cantidad_productos = faker.number.int({
      min: 1,
      max: productos_maximos_por_distribuidor,
    });
    for (let p = 0; p < cantidad_productos; p++) {
      const nombre_producto = faker.commerce.productName();
      const precio_producto = faker.number.int({ min: 100, max: 10000 });

      await conexion.execute(
        "INSERT INTO producto (nombreProducto, precio, idDistribuidor) VALUES (?, ?, ?);",
        [nombre_producto, precio_producto, idDistribuidor]
      );
    }
  }

  console.log("Datos generados y almacenados correctamente");
} catch (error) {
  console.error("Error durante el poblado:", error);
} finally {
  await conexion.end();
  console.log("Conexión cerrada.");
}
