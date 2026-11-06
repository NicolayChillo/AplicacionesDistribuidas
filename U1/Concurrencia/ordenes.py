# Simulación de un proceso de pago que tarda un tiempo variable en completarse.
import asyncio
import time

async def procesar_pago(id_orden, tiempo_espera):
    print(f"[Orden {id_orden}] Iniciando conexión con la pasarela de pagos...")
    
    await asyncio.sleep(tiempo_espera)
    
    print(f"[Orden {id_orden}] Pago procesado con éxito (tomó {tiempo_espera}s).")

async def main():
    print("----------------- SISTEMA DE PAGOS ----------------- ")
    inicio = time.time()
    
    print("Procesando múltiples órdenes de compra al mismo tiempo...\n")

    await asyncio.gather(
        procesar_pago(101, 3),
        procesar_pago(102, 1),
        procesar_pago(103, 2)
    )
        
    tiempo_total = time.time() - inicio
    print(f"Todas las transacciones finalizadas.")
    print(f"Tiempo total asíncrono: {tiempo_total:.2f} segundos.")

if __name__ == "__main__":
    asyncio.run(main())