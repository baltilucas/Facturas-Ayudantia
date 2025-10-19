CREATE TABLE cliente(
    idCliente INT PRIMARY KEY AUTO_INCREMENT,
    nombreCliente varchar(100) NOT NULL,
    correo varchar(200)
);

CREATE TABLE distribuidor(
    idDistribuidor INT PRIMARY KEY AUTO_INCREMENT,
    nombreDistribuidor varchar(100)
);

CREATE TABLE factura(
    idFactura INT PRIMARY KEY AUTO_INCREMENT,
    idCliente INT,
    fecha timestamp,
    FOREIGN KEY (idCliente) REFERENCES cliente(idCliente)
);

CREATE TABLE producto(
    idProducto INT PRIMARY KEY AUTO_INCREMENT,
    nombreProducto varchar(100),
    precio INT not null,
    idDistribuidor INT,
    FOREIGN KEY (idDistribuidor) REFERENCES distribuidor(idDistribuidor)
);

CREATE TABLE venta(
    idFactura INT,
    idProducto INT,
    cantidad INT,
    descuento FLOAT,
    PRIMARY KEY (idFactura, idProducto),
    FOREIGN KEY (idFactura) REFERENCES factura(idFactura),
    FOREIGN KEY (idProducto) REFERENCES producto(idProducto)
);