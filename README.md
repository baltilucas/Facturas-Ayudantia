# Facturas-Ayudantia

Aquí se guardará el registro del ejemplo a llevar en varias clases de ayudantía del ejemplo de un sistema generico de facturas.

![Modelo De BDD de un sistema generico de facturas](modelo.png)

Se ejemplificará con el trabajo de instancias EC2, no obstante la gran mayoría de contenido es genérico MySQL, MariaDB y demás motores similares.

## Trabajo con instancias EC2

Se crea una instancia EC2 desde AWS, se recomienda usar micro pues la capa gratuita dura 1 hora y se puede borrar, reduciendo así los costos.

### SSH

Si se quiere trabajar desde el computador personal, se puede realizar una conexión via ssh que permite utilizar la terminal del equipo como si fuera la de la instancia.

Para esto al momento de crear la instancia se permite crear un par de claves, se recomienda usar .pem que permite usar ssh sin usar PUTTY necesariamente.

Al crear el archivo para conectarse se selecciona la opción cliente SSH en el entorno AWS que da el instructivo.

### Inicio de Configuración de entorno
Al iniciar la instancia por primera vez, se comienza **SIEMPRE** con:
 - `sudo apt update`
 - `sudo apt upgrade -y`

Se puede verificar que git esté instalado con `git --version`

Para instalar MySQL dentro de la instancia:

`sudo apt install mysql-server -y`

Al crearlo en la instancia no se configura automaticamente el usuario _root_, debido a esto se crea uno mediante la interfaz de MySQL. 

- Para abrir el MySQL sin usuario creado: `sudo mysql`
- Para crear usuario desde MYSQL `CREATE USER 'root'@'localhost' IDENTIFIED BY '<tu-clave>';`
- Para dar acceso a usuario: `GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION;`


### Comandos Básicos

- Ver bases de datos: `SHOW DATABASES;`
- Seleccionar una base de datos: `USE <nombreDB>;`
- Crear una base de datos: `CREATE DATABASE <nombreDB>;`
- Crear una tabla cuando se usa una base de datos: `CREATE TABLE <Nombre>;`


