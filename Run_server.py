import subprocess
import webbrowser
import socket

# Obtener la dirección IP
ip_address = socket.gethostbyname(socket.gethostname())

# Ejecutar el servidor HTTP en un proceso separado
server_process = subprocess.Popen(['python', '-m', 'http.server', '8000'])

# URL de la página principal
url = f'http://{ip_address}:8000/'

# Abrir el navegador con la dirección IP
webbrowser.open(url)

# Mostrar mensaje al usuario
print(f"El servidor se está ejecutando. Puedes acceder a tus archivos en: {url}")

# Esperar a que el usuario decida cerrar el servidor
input("Presiona Enter para detener el servidor...")

# Detener el servidor HTTP
server_process.terminate()
