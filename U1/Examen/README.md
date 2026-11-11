# Chat en Tiempo Real con Sockets, Hilos y Docker

Esta es una aplicación de chat en tiempo real desarrollada en Python. Utiliza Sockets TCP para la red y Multithreading para lograr una comunicación asíncrona, por lo que los usuarios pueden escribir y recibir mensajes sin esperar turnos.

## Requisitos
- Docker y Docker Compose instalados.
- Python 3 instalado en la máquina anfitriona con la que se podra ejecutar clientes.
- Visual Studio Code.

## Pasos para ejecutar la práctica

### Paso 1: Iniciar el Servidor (En Docker)
El servidor se ejecuta en un contenedor. Para permitir que el servidor también pueda enviar mensajes con una entrada interactiva, inícialo con el siguiente comando en una terminal:

```bash
docker-compose run --name servidor_chat --service-ports servidor
```

### Paso 2: Iniciar clientes
El servidor esperara la conexión de los clientes, por lo que en varias terminales de VS puedes ejecutar un cliente nuevo que se conectaran de manera simulatanea al servidor y podran interactuar entre ellos y el servidor.

Para ejecutar el archivo coloca el siguiente comando en la terminal:

```bash
python cliente.py
```

Esto para cada cliente que tendra su propia terminal.

### Paso 3: Conversación
En cada terminal ya sea del cliente o el servidor podras enviar y recibir el mensaje de los demas, y si alguno de los clientes desea terminar el chat, puede escribir **salir**, esto hará que termine la conexión. De igual manera, el servidor si desea desconectar toda la interacción, escribira **salir**, haciendo que notifique a los clientes que el servidor fue desconectado y terminara su ejecució.

## Nota
Si se desea ejecutar de nuevo el servidor, ejecute el siguiente comando. De está manera solo inicializa el servidor y podra interactuar de nuevo.

```bash
docker start -ai servidor_chat
```