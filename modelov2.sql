CREATE TABLE cliente(
    idCliente INT PRIMARY KEY AUTO_INCREMENT,
    nombreCliente varchar(100) NOT NULL,
    correo varchar(200)
);

CREATE TABLE pais(
    idPais INT PRIMARY KEY AUTO_INCREMENT,
    nombrePais varchar(100)
);

INSERT INTO
    pais(nombrePais)
VALUES
    ('Argentina'),
    ('Brasil'),
    ('Chile'),
    ('Uruguay'),
    ('Paraguay'),
    ('China'),
    ('Estados Unidos'),
    ('Canada'),
    ('Mexico'),
    ('Colombia');

CREATE TABLE distribuidor(
    idDistribuidor INT PRIMARY KEY AUTO_INCREMENT,
    nombreDistribuidor varchar(100),
    idPais INT,
    FOREIGN KEY (idPais) REFERENCES pais(idPais)
);

CREATE TABLE factura(
    idFactura INT PRIMARY KEY AUTO_INCREMENT,
    idCliente INT,
    fechaHora timestamp,
    FOREIGN KEY (idCliente) REFERENCES cliente(idCliente)
);

CREATE TABLE tipoproducto(
    idTipoProducto INT PRIMARY KEY AUTO_INCREMENT,
    tipoProducto varchar(100)
);

INSERT INTO
    tipoproducto(tipoProducto)
VALUES
    ('Alimento'),
    ('Vestuario'),
    ('Jardineria'),
    ('Muebleria'),
    ('Jugueteria');

CREATE TABLE producto(
    idProducto INT PRIMARY KEY AUTO_INCREMENT,
    nombreProducto varchar(100),
    precio INT not null,
    idTipoProducto INT,
    idDistribuidor INT,
    FOREIGN KEY (idDistribuidor) REFERENCES distribuidor(idDistribuidor),
    FOREIGN KEY (idTipoProducto) REFERENCES tipoproducto(idTipoProducto)
);

CREATE TABLE venta(
    idFactura INT,
    idProducto INT,
    cantidad INT,
    descuento FLOAT,
    vencimiento date,
    PRIMARY KEY (idFactura, idProducto),
    FOREIGN KEY (idFactura) REFERENCES factura(idFactura),
    FOREIGN KEY (idProducto) REFERENCES producto(idProducto)
);