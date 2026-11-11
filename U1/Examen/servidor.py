import socket
import threading
import sys
import time

# Configuración del servidor
HOST = '0.0.0.0'  # conexiones externas al contenedor
PORT = 5000

clientes = [] # Lista de clientes
contador_clientes = 0 # contador para asignar numeracion a cliente

def manejar_cliente(conexion, nombre):
    
    ## Ejecucion de un hilo por cada cliente, recibir y retransmitir
    while True:
        try:
            # Recibe hasta 1024 bytes del cliente
            datos = conexion.recv(1024)
            if not datos:
                break # Si no hay datos, el cliente se desconectó
            
            # Decodifica el mensaje y le añade la etiqueta del cliente
            mensaje = datos.decode('utf-8')
            mensaje_formateado = f"[{nombre}]: {mensaje}"
            
            # Muestra el mensaje en la consola del servidor
            print(mensaje_formateado)
            
            # Retransmite el mensaje a los otros clientes
            difundir(mensaje_formateado, conexion)
        except:
            break
    
    # Desconexión si el bucle se rompe
    conexion.close()
    clientes.remove((conexion, nombre))
    mensaje_salida = f"[SERVIDOR]: {nombre} ha abandonado el chat."
    print(mensaje_salida)
    difundir(mensaje_salida, None)

def difundir(mensaje, remitente_conexion):   
    # Envía un mensaje a todos los clientes conectados, excepto al que lo envió.
    #Si remitente_conexion es None, el mensaje es del propio servidor y se envía a todos.
    
    for cliente_conn, _ in clientes:
        if cliente_conn != remitente_conexion:
            try:
                cliente_conn.sendall(mensaje.encode('utf-8'))
            except:
                pass

def recibir_conexiones(servidor):
    # Hilo dedicado exclusivamente a aceptar nuevas conexiones sin bloquear el servidor.
    global contador_clientes
    while True:
        try:
            conexion, direccion = servidor.accept()
            contador_clientes += 1
            nombre = f"CLIENTE {contador_clientes}"
            
            # Añadimos el nuevo cliente a la lista
            clientes.append((conexion, nombre))
            print(f"[SERVIDOR]: Se conectó {nombre} desde {direccion}")
            
            # Avisamos a los otros que alguien entró
            difundir(f"[SERVIDOR]: {nombre} se ha unido al chat.", conexion)
            
            # Le damos la bienvenida al cliente y le decimos quien es
            conexion.sendall(f"[SERVIDOR]: Bienvenido, eres el {nombre}\n".encode('utf-8'))
            
            # Creamos un hilo independiente para escuchar los mensajes de este nuevo cliente
            hilo_cliente = threading.Thread(target=manejar_cliente, args=(conexion, nombre), daemon=True)
            hilo_cliente.start()
        except:
            break

def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Permite reutilizar el puerto
    servidor.bind((HOST, PORT))
    servidor.listen(5) # Acepta hasta 5 conexiones en espera
    
    print(f"[SERVIDOR] Iniciado y escuchando en el puerto {PORT}")
    print("Escribe tus mensajes aquí para enviarlos a todos los clientes (Escribe 'salir' para cerrar):\n")
    
    # Iniciamos el hilo que acepta conexiones en segundo plano
    hilo_conexiones = threading.Thread(target=recibir_conexiones, args=(servidor,), daemon=True)
    hilo_conexiones.start()
    
    # El hilo principal se queda leyendo lo que escriba el servidor para enviarlo a los clientes
    try:
        while True:
            try:
                mensaje = input()
                if mensaje.lower() == 'salir':
                    break
                mensaje_formateado = f"[SERVIDOR]: {mensaje}"
                difundir(mensaje_formateado, None)
            except EOFError:
                # Si se corre en Docker sin terminal interactiva, evitamos que crashee
                time.sleep(1) 
    except KeyboardInterrupt:
        print("\n[SERVIDOR] Apagando...")
    finally:
        servidor.close()
        sys.exit(0)

if __name__ == "__main__":
    iniciar_servidor()