import threading
import time

def subproceso(condicion):
    while not condicion.is_set():
        time.sleep(2)
        print("\nProceso en segundo plano...")

condicion = threading.Event()                                                   #crear flag para permitir cortarlo

while True:
    print("""
1) Iniciar proceso en segundo plano
2) Salir\n
    """)
    entrada = input("->")
    
    if entrada == "1":
        hilo = threading.Thread(target = subproceso, args = (condicion,))       #Thread es una clase
        hilo.start()                                                            #inicia la ejecución

    if entrada == "2":
        condicion.set()                                                         #corta la ejecución del hilo de arriba
        hilo.join()                                                             #espera a que termine la ejecución y ahí corta
        break