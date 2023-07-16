import numpy as np
from asistente import *

def marcar(arreglo_asistente ):
    x = 1
    for f in range(10):
        for c in range(10):
            if len(str(x)) == 1:
                arreglo_asistente[f][c] = '0' + str(x)
            else:
                arreglo_asistente[f][c] = str(x)
            x +=1
def llenar(arreglo_asistente):
    x = 1
    for f in range(10):
        for c in range(10):
            if len(str(x)) == 1:
                arreglo_asistente[f][c] = '0' + str(x)
            else:
                arreglo_asistente[f][c] = str(x)
            x += 1



def mostrar(arreglo_asistente):
    for f in range(10):
        fila = ''
        for c in range(10):
            fila = fila + ' | ' + arreglo_asistente[f][c]
        print(fila)


def marcar(arreglo_asistente, num_asiento):
    x = 1
    for f in range(10):
        for c in range(10):
            if x == num_asiento:
                 arreglo_asistente[f][c] = 'XX'
            x += 1


def verificar_asiento(arreglo_asiento, num_asiento):
    x = 1
    for f in range(10):
        for c in range(10):
            if x == num_asiento:
                if arreglo_asiento[f][c] == 'XX':
                    return False
            x += 1

def validar_rut():
    while True:
        try:
            rut = int(input("ingrese rut:"))
            if len(str(rut)) == 0:
                return True
            else:
                print("rut incorrecto:")
        except BaseException as error:
            print(f"error:{error}")


def ingresar_asistente(lista_asistente, num_asiento):
    asi = asistente
    asi.rut= validar_rut()
    asi.nombre = input("ingrese nombre")
    asi.num_asiento = num_asiento
    if num_asiento >= 1 and num_asiento <=20:
        asi.valor_asiento = 120000
    if num_asiento >= 21 and num_asiento <=50:
        asi.valor_asiento = 80000
    if num_asiento >= 51 and num_asiento <=100:
        asi.valor_asiento = 50000
    lista_asistente.append(asi)

def listado(lista_asistente):
    print("listado de asistencias")
    print("----------------------")
    for asi in lista_asistente:
        print("listado de asistentes")
        print("---------------------")


def ganancias(lista_asistente):
    print("ganancias de asistentes")
    print("---------------------")
    platinum = 0
    gold = 0
    silver = 0
    for asi in lista_asistente:
        if int(asi.valor_asiento) == 120000:
            platinum += 1
        if int(asi.valor_asiento) == 80000:
            gold += 1
        if int(asi.valor_asiento) == 50000:
            silver += 1
    print(f"total platinum: {platinum} valor:{platinum+120000}")

    print(f"total gold: {gold} valor:{gold+80000}")

    print(f"total silver:  {silver} valor:{silver+50000}")
    total_asi = platinum + gold + silver
    total_val = (platinum+120000) + (gold+80000) + (silver+50000)
    print(f"total asistente : {total_asi}")
    print(f"total valor:      {total_val}")

def comprar(arreglo_asistente, lista_asistente):
    compra = 0
    try:
        cant=int(input("ingese cantidad destino:"))
        if cant >= 1 and cant <= 5:
            while compra < cant:
                print("ubicacion de asiento")
                mostrar(arreglo_asistente)
                print(f"seleccione {cant} de asiento:")
                try:
                    num_asiento= int(input("ingrese el numero de asiento"))
                    if num_asiento >= 1 and num_asiento <=10:
                        resp =verificar_asiento(arreglo_asistente, num_asiento)
                        if resp == True:
                            marcar(arreglo_asistente, num_asiento)
                            ingresar_asistente((lista_asistente, num_asiento))
                            compra += 1
                        else:
                            print("asiento no disponible")
                except BaseException as error:
                    print(f"error {error}")
                else:
                    print("la cantidad debe estar entre 1 y 5")
    except BaseException as error:
        print(f"error:{error}")

def comprar_entradas():
    x = 1


def salir():
    print("Copyright= Gustavo Marchant INC.2023 V.03 16/07/2023")
    return False