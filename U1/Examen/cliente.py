import socket
import threading

# Dirección del servidor, el puerto de Docker se expone a localhost.
HOST = '127.0.0.1'
PORT = 5000 

# Variable global para controlar el estado de la conexión
conectado = True

def recibir_mensajes(cliente):
    #Hilo en segundo plano que escucha constantemente si llegan mensajes del servidor
    global conectado
    while conectado:
        try:
            datos = cliente.recv(1024)
            if not datos:
                if conectado:
                    print("\n[SERVIDOR DESCONECTADO]")
                break
            # Imprimimos el mensaje recibido
            print(f"\n{datos.decode('utf-8')}")
            # Volvemos a imprimir "Tú: " para que la consola no se vea fea tras recibir un mensaje
            print("Tú: ", end="", flush=True) 
        except (OSError, socket.error):
             # Solo muestra error si la desconexión NO fue iniciada por el usuario
            if conectado:
                print("\n[ERROR DE CONEXIÓN INESPERADO]")
                conectado = False
            break       
        except Exception:
            break

def iniciar_cliente():
    global conectado
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Intentamos conectar al puerto expuesto por Docker
        cliente.connect((HOST, PORT))
    except Exception as e:
        print(f"Error al conectar con el servidor: {e}")
        return
    
    print("Conectado al chat. Puedes empezar a escribir. (Escribe 'salir' para terminar)")
    
    # Iniciamos el hilo que se encarga exclusivamente de recibir mensajes
    hilo_recepcion = threading.Thread(target=recibir_mensajes, args=(cliente,), daemon=True)
    hilo_recepcion.start()
    
    # El hilo principal se encarga de leer el teclado del usuario y enviar el texto
    try:
        while conectado:
            mensaje = input("Tú: ")
            if mensaje.lower() == 'salir':
                break
            # Enviamos el mensaje codificado en bytes
            cliente.sendall(mensaje.encode('utf-8'))
    except (KeyboardInterrupt, EOFError):
        conectado = False
    finally:
        # Notificamos al hilo de recepción que el cierre es voluntario
        conectado = False
        
        # Cerramos los canales del socket limpiamente para interrumpir el recv()
        try:
            cliente.shutdown(socket.SHUT_RDWR)
        except:
            pass
        
        cliente.close()
        print("Saliendo del chat...")

if __name__ == "__main__":
    iniciar_cliente()