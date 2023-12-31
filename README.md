# Servidor HTTP Simple
Este script de Python te permite ejecutar un servidor HTTP simple en tu máquina local y acceder a tus archivos a través de un navegador web. Utiliza el módulo **http.server** para proporcionar acceso a los archivos en el directorio actual.

## Requisitos
Asegúrate de tener instalado Python en tu sistema. Puedes descargar Python desde [python.org](https://www.python.org/).

## Ejecución
1. Clona o descarga este repositorio a tu máquina local.

2. Coloca los archivos que deseas compartir en la misma carpeta que contiene el archivo Python **(Run_server.py)**.

3. Ejecuta el archivo. Si estás utilizando una terminal, navega hasta el directorio donde se encuentra el archivo Python.

4. Si estás utilizando una terminal, ejecuta el siguiente comando:

    ``` bash
    python Run_server.py
    ``` 
    El servidor se iniciará y mostrará la dirección IP junto con el puerto en el que está sirviendo los archivos.

5. Se abrirá automáticamente un navegador web con la dirección IP proporcionada. Si no se abre automáticamente, puedes acceder a tus archivos utilizando la URL mostrada en la terminal.

## Detener el servidor
Para detener el servidor, simplemente regresa a la terminal donde se está ejecutando el script y presiona Enter. Esto detendrá el servidor HTTP.

## Notas
- Este servidor HTTP sirve los archivos del directorio en el que se encuentra el script. Asegúrate de tener los archivos que deseas acceder en este directorio.
- Ten en cuenta que este servidor es para propósitos de desarrollo local. No se recomienda para un entorno de producción debido a sus limitaciones de seguridad y rendimiento.

¡Disfruta accediendo a tus archivos a través de tu navegador con este servidor simple!
