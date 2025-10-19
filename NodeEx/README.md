# Ejemplo de trabajo en Node

A continuación está un script de como sería el trabajo de este proyecto en un entorno NodeJs, para utilizarlo se necesita tener descargado al menos la versión 20.19.

Esto es relevante pues en la actualidad el Framework de desarrllo más utilizado en el mundo es Node, debido a que permite desarrollo web, local, entrenamiento de IA y se puede ejecutar distribuidamente con facilidad.


## Instructivo instalación Node

Para trabajar con NodeJS es posible descargar e instalarlo directamente, pero se recomienda utilizar un controlador de versiones para así poder mantener aplicaciones legacy o varios proyectos a la vez.

Existen múltiples controladores de versiones, pero se dará el ejemplo con 2 entornos principales: NVM (Node Version Manager) y FNM (Fast Node Manager).

### NVM

Es más complejo de usar en entornos fuera de la familia linux debido a que fue desarrollado para esta, especialmente pensando en servidores donde se tiene un entorno gráfico mínimo.

Su ventaja es que tiene una sintaxis más acotada y su manejo de versiones es un poco menos complejo, su gestor de paquetes es npm.

Se recomienda para instalar en entornos EC2 por lo mismo, para instalarlo en maquinas Ubuntu, amazon Linux, pc con distribuciones de la familia o en windows con _WSL_ se puede usar el comando

```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
```

Posteriormente se verifica instalación con 

```
nvm -v
```

Luego para instalar una versión de node se utiliza:

```
nvm install 20
```

Esto por ejemplo instala la versión 20 en su actualización estable, en caso de querer usarse una en particular se puede ingresar el número completo.

Finalmente para usar la versión instala se utiliza

```
nvm use 20
```

Donde se usará la instalada por defecto, existen más opciones de configuración pero esto es lo básico.

### FNM

Es la más sencilla de instalar en varios entornos de desarrollo, tanto linux, mac o windows por lo que suele ser predilecta en muchos cursos online, su instalación es rápida y tiene soporte en varios gestores de paquetes como winget, choco, brew, scoop entre otros.

Para intalar se recomienda seguir las instrucciones disponibles en https://github.com/Schniz/fnm.

Respecto a los comandos de instalación de versiones su uso es análogo a NVM pero utilizando `fnm` en vez de `nvm`