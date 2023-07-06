import numpy as np
from Creativo import *
from Funciones import *

arreglo = np.full((10,10), '---')
lista_asistente = []
ciclo=True





###########

def agregarAsistente(lista_asistente, num_ubicacion):
    a = Creativo()
    a.rut = int(input("Ingrese Rut:"))
    a.nombre = input("Ingrese Nombre:")
    a.apellido= input("Ingrese Apellido:")
    a.edad= int(input("Ingrese Edad:"))
    a.num_ubicacion = num_ubicacion
    if num_ubicacion>=1 and num_ubicacion<=20:
        a.valor=120000
    if num_ubicacion>=21 and num_ubicacion<=50:
        a.valor=80000
    if num_ubicacion>=51 and num_ubicacion<=100:
        a.valor=50000
    lista_asistente.append(a)




def comprarEntrada(arreglo,lista_asistente):
    try:
        ubicaciones = int(input("Ingrese Ubicaciones (1-3):"))
        if ubicaciones>=1 and ubicaciones<=3:
            compra = 0
            while compra<ubicaciones:
                mostrar(arreglo)
                num_ubicacion = int(input("Numero de Ubicacion:"))
                if num_ubicacion>=1 and num_ubicacion<=100:
                    disponible = comprobarUbicacion(arreglo, num_ubicacion)
                    if disponible == True:
                        agregarAsistente(lista_asistente, num_ubicacion)
                        comprar(arreglo, num_ubicacion)
                        compra = compra + 1
                    else:
                        print("No esta disponible")
                else:
                    print("Numero de Ubicacion de 1 a 100")
        else:
            print("Ubicaciones entre 1 a 3")
    except BaseException as error:
        print(f"Error:{error}")



llenar(arreglo)

def listarAsistente(lista_asistente):
    for per in lista_asistente:
        print(f"Nombre:{per.nombre} Valor:${per.valor} Ubicacion:{per.num_ubicacion}")


def totales(lista_asistente):
    p=0
    g=0
    s=0
    tot_p=0
    tot_g=0
    tot_s=0
    for Creativo in lista_asistente:
        if int(Creativo.valor) == 120000:
            p = p + 1
            tot_p = tot_p + 120000
        if int(Creativo.valor) == 80000:
            g = g + 1
            tot_g = tot_g + 80000
        if int(Creativo.valor) == 50000:
            s = s + 1
            tot_s = tot_s + 50000
        print(f"Platinum: Cantidad:{p} Total:${tot_p}")
        print(f"Gold:     Cantidad:{g} Total:${tot_g}")
        print(f"Silver:   Cantidad:{s} Total:${tot_s}")

def salir():
    print("Adhemar Morales")
    print("06/07/2023")

while ciclo:
    print("Creativos.cl")
    print("1) Comprar Entradas")
    print("2) Mostrar Ubicaciones Disponibles")
    print("3) Ver Listado de Asistentes")
    print("4) Mostrar Ganancias Totales")
    print("5) Salir")
    try:
        op=int(input("Seleccione (1-5):"))
        match op:
            case 1:
                comprarEntrada(arreglo, lista_asistente)
            case 2:
                mostrar(arreglo)
            case 3:
                listarAsistente(lista_asistente)
            case 4:
                totales(lista_asistente)
            case 5 :
                ciclo = salir()
    except BaseException as error:
        print(f"Error:{error}")

