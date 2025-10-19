INSERT INTO venta (idFactura, idProducto, cantidad, descuento)
SELECT 
    f.idFactura,
    (SELECT idProducto FROM producto ORDER BY RAND() LIMIT 1) AS idProducto,
    FLOOR(RAND() * (10 - 5 + 1)) + 5 AS cantidad,
    0 AS descuento
FROM factura f;
select count(*) from venta;
