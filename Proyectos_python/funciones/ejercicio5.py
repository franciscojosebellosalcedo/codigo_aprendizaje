import time
import os
time.sleep(1)
os.system("cls")


def Maximin():
    array = []
    ingrese = int(input("ingrese la cantidad de datos que va a introducir:"))
    for x in range(1, ingrese):
        datos = int(input(f"digite valor {x} :"))
        array.append(datos)
    mayor = array[0]
    for i in range(len(array)):
        if(array[i] > mayor):
            mayor = array[i]
    print("El valor maximo es:", mayor)

    menor = array[0]
    for i in range(len(array)):
        if(array[i] < menor):
            menor = array[i]
    print("El valor minimo es:", menor)


Maximin()
        

        
    

