import subprocess
import webbrowser
import socket
import sys

try:
    import psutil
except ImportError:
    print("El módulo 'psutil' no está instalado. Instalándolo ahora...")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'psutil'])
    import psutil

def get_active_ip_addresses():
    """Obtiene las direcciones IP IPv4 de las interfaces activas de la máquina local junto con sus nombres."""
    addresses = []
    # Obtener el estado de las interfaces
    stats = psutil.net_if_stats()
    for interface_name, addrs in psutil.net_if_addrs().items():
        # Verificar si la interfaz está activa
        if interface_name in stats and stats[interface_name].isup:
            for addr in addrs:
                if addr.family == socket.AF_INET:
                    ip = addr.address
                    if ip != '127.0.0.1':
                        addresses.append((interface_name, ip))
    return addresses

def is_port_in_use(port):
    """Verifica si el puerto está en uso."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

# Puerto inicial
port = 8000

# Intentar iniciar el servidor en el puerto especificado
while True:
    if not is_port_in_use(port):
        try:
            # Ejecutar el servidor HTTP en un proceso separado
            server_process = subprocess.Popen(
                [sys.executable, '-m', 'http.server', str(port), '--bind', '0.0.0.0'],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.STDOUT
            )
            break  # Salir del bucle si el servidor se inicia correctamente
        except Exception as e:
            print(f"Ocurrió un error al iniciar el servidor: {e}")
            port_input = input("Ingresa otro número de puerto: ")
            try:
                port = int(port_input)
            except ValueError:
                print("Por favor, ingresa un número válido de puerto.")
    else:
        print(f"El puerto {port} está en uso.")
        port_input = input("Ingresa otro número de puerto: ")
        try:
            port = int(port_input)
        except ValueError:
            print("Por favor, ingresa un número válido de puerto.")

# Obtener todas las direcciones IP activas junto con sus interfaces
ip_addresses = get_active_ip_addresses()

if ip_addresses:
    # Mostrar todas las URL posibles con sus interfaces activas
    print("El servidor se está ejecutando en las siguientes direcciones (interfaces activas):")
    for interface_name, ip in ip_addresses:
        url = f'http://{ip}:{port}/'
        print(f"- {url} (Interfaz: {interface_name})")
    # Abrir el navegador con la primera dirección IP activa
    webbrowser.open(f'http://{ip_addresses[0][1]}:{port}/')
else:
    print("No se encontraron direcciones IP activas disponibles para mostrar.")

# Asegurar que el mensaje se imprime en una nueva línea
print()

# Esperar a que el usuario decida cerrar el servidor
input("Presiona Enter para detener el servidor...\n")

# Detener el servidor HTTP
server_process.terminate()
