from asistente import *
from funciones import *
import numpy as np

arreglo_asistente = np.full((10,10), '-----')
lista_asistente=[]
############################################
ciclo = True
llenar(arreglo_asistente)
while ciclo:
    print("Creativos.cl")
    print("1) Comprar entradas")
    print("2) Mostrar ubicacion disponible")
    print("3) Ver listado de asistencia")
    print("4) Mostrar ganancias totales")
    print("5) Salir")
    try:
        op=int(input("Seleccione(1-5):"))
        match op:
            case 1:
                comprar(arreglo_asistente, lista_asistente)
            case 2:
                mostrar(arreglo_asistente)
            case 3:
                listado(lista_asistente)
            case 4:
                ganancias(lista_asistente)
            case 5:
                ciclo = salir()
            case _:
                print("opcion incorrecta")


    except BaseException as error:
        print(f"error:{error}")
