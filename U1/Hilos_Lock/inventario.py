
import time
import threading

stock_cosmetico = 100 # unidades en inventario

lock = threading.Lock()

def procesar_compra(id_cliente, cantidad_solicitada):
    global stock_cosmetico
    
    print(f"[Cliente {id_cliente}] Intenta comprar {cantidad_solicitada} unidades...")
    
    with lock:
        stock_actual = stock_cosmetico
        
        time.sleep(0.5) # tiempo de procesamiento simulado

        # verificar si hay suficiente stock
        if stock_actual >= cantidad_solicitada:
            stock_cosmetico = stock_actual - cantidad_solicitada
            print(f"[Cliente {id_cliente}] Compra exitosa. Stock restante: {stock_cosmetico}")
        else:
            print(f"[Cliente {id_cliente}] Error: Stock insuficiente. Solo quedan {stock_actual}.")

def main():
    print(" --------------- SISTEMA DE INVENTARIO --------------- ")
    print(f"Stock inicial en bodega: {stock_cosmetico} unidades\n")
    
    hilos = []
    
    # 4 clientes intentan comprar 30 unidades cada uno al mismo tiempo
    for i in range(1, 5):
        hilo = threading.Thread(target=procesar_compra, args=(i, 30))
        hilos.append(hilo)
        hilo.start()
        
    for hilo in hilos:
        hilo.join()
        
    print(f"\n Transacciones finalizadas. Stock final: {stock_cosmetico}")

if __name__ == "__main__":
    main()