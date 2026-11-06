# Simulacion de preparacion de un desayuno
import time

def hervir_agua():
    print("1. Iniciando: Hervir agua para el café...")
    time.sleep(3)
    print("   Terminado: El agua está hirviendo.")

def tostar_pan():
    print("2. Iniciando: Tostar las rebanadas de pan...")
    time.sleep(4)
    print("   Terminado: El pan está tostado.")

def freir_huevos():
    print("3. Iniciando: Freír los huevos...")
    time.sleep(5)
    print("   Terminado: Los huevos están listos.")

def servir_desayuno():
    print("4. Iniciando: Sirviendo todo en la mesa...")
    time.sleep(2)
    print("   Terminado: Desayuno servido.")

def main():
    print("INICIO DE LA PREPARACIÓN DEL DESAYUNO")
    inicio = time.time()
    
    hervir_agua()
    tostar_pan()
    freir_huevos()
    servir_desayuno()
    
    fin = time.time()
    tiempo_total = fin - inicio
    
    print(f"Proceso completado. Tiempo total de ejecución: {tiempo_total:.2f} segundos.")

if __name__ == "__main__":
    main()