# Aplicaciones Distribuidas - Ejercicios Unidad 1

Este repositorio contiene la resolución de las 3 asignaciones correspondientes a la Unidad 1. En estos ejercicios se demuestran diferentes paradigmas de ejecución de procesos utilizando Python y orquestación con Docker Compose.

## 📁 Enlaces a las Asignaciones (Carpetas)

A continuación, los accesos directos a cada uno de los ejercicios solicitados:

1. 🥞 **[Ejercicio 1: Ejecución Secuencial](./Secuencial)** 
   - **Script:** `desayuno.py`
   - **Descripción:** Demostración de un modelo bloqueante simulando la preparación de un desayuno, donde cada tarea debe finalizar completamente antes de que inicie la siguiente.

2. 📨 **[Ejercicio 2: Ejecución Concurrente](./Concurrencia)** 
   - **Script:** `ordenes.py`
   - **Descripción:** Implementación de procesamiento asíncrono utilizando `asyncio`. Simula el procesamiento de múltiples órdenes de compra al mismo tiempo mediante un bucle de eventos (event loop).

3. 🛒 **[Ejercicio 3: Hilos con Lock (Condición de Carrera)](./Hilos_Lock)** 
   - **Script:** `inventario.py`
   - **Descripción:** Simulación de un sistema de inventario transaccional. Utiliza `threading` y `Lock` para proteger una variable compartida (el stock) y evitar inconsistencias cuando múltiples clientes compran simultáneamente.

---

## 🚀 Cómo ejecutar los ejercicios

Tienes dos opciones para probar los scripts: utilizando la infraestructura de Docker o ejecutando directamente los archivos de Python.

### Opción A: Usando Docker Compose (Recomendado)

Toda la infraestructura está configurada para levantarse fácilmente. Los tres servicios están definidos en el archivo `docker-compose.yml` ubicado dentro de la carpeta `U1`.

1. Clona el repositorio y entra a la carpeta `U1`:
   ```bash
   git clone https://github.com/NicolayChillo/AplicacionesDistribuidas.git
   cd AplicacionesDistribuidas/U1
   ```

2. Ejecuta cada ejercicio con los siguientes comandos (el flag `--build` asegura que Docker lea siempre tu código más reciente):

   **Ejercicio 1: Secuencial (`desayuno.py`)**
   ```bash
   docker-compose up --build ejercicio_secuencial
   ```

   **Ejercicio 2: Concurrencia (`ordenes.py`)**
   ```bash
   docker-compose up --build ejercicio_concurrencia
   ```

   **Ejercicio 3: Hilos con Lock (`inventario.py`)**
   ```bash
   docker-compose up --build ejercicio_hilos
   ```

3. Al terminar, limpia los contenedores con:
   ```bash
   docker-compose down
   ```

---

### Opción B: Ejecución directa con Python (Sin Docker)

Si prefieres correr los archivos `.py` directamente en tu máquina (asegúrate de tener Python 3 instalado):

1. Clona el repositorio y entra a la carpeta `U1`:
   ```bash
   git clone https://github.com/NicolayChillo/AplicacionesDistribuidas.git
   cd AplicacionesDistribuidas/U1
   ```

2. Ejecuta cada archivo indicando su ruta:
   
   **Secuencial:**
   ```bash
   python Secuencial/desayuno.py
   ```
   
   **Concurrencia:**
   ```bash
   python Concurrencia/ordenes.py
   ```
   
   **Hilos con Lock:**
   ```bash
   python Hilos_Lock/inventario.py
   ```