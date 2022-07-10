from ast import Try
import time
import os
os.system("cls")
time.sleep(1)



def Menu():
    print("----------TIENDA ISCO----------")
    print(" ")
    print("[1]:ingresar datos.")
    print("[0]:para salir del programa.")
Menu()
print("\n")
def Ingresar():
    opcion=int(input("Digite  opcion:"))
    while(opcion<0 or opcion>1):
        print("Error. Opcion incorrecta.")
        opcion=int(input("Digite la opcion nuevamente:"))
    if (opcion == 0):
        exit()
    if (opcion==1):
        inventario=[ ]
        aux=0
        while(aux!=1):
            nombre=input("ingrese el nombre del producto: ")
            cantidad=int(input("ingrese la cantidad de productos:"))
            while(cantidad<=0):
                print("Cantidad no correspondiente.")
                cantidad = int(input("ingrese la cantidad de productos nuevamente:"))
            precio=float(input("ingrese el precio del producto:"))
            while(precio<=0):
                print("Precio no valido.")
                precio = float(input("ingrese el precio del producto nuevamente:"))
            unidad_medida=input("ingrese la unidad de medida:")
            referencia=input("ingrese la referencia del producto:")
            fecha_ingreso=input("ingrese la fecha de ingreso del producto:")
            fecha_vencimiento=input("ingrese la fecha de vencimiento del producto:")
            inventario.append([nombre,cantidad,precio,unidad_medida,referencia,fecha_ingreso,fecha_vencimiento])
            aux=int(input("Digite 0 para agregar mas datos \n Digite 1 para salir del programa:"))

    for i in range(len(inventario)):
        print("Nombre del producto:",inventario[i][0],"\n",
            "Cantidad del producto:",inventario[i][1],"\n",
            "Precio:",inventario[i][2],"\n",
            "Unidad de medida:",inventario[i][3],"\n",
            "Referencia:",inventario[i][4],"\n",
            "Fecha de ingreso:",inventario[i][5],"\n",
            "Fecha de vencimiento:",inventario[i][6])

print("\n") 

Ingresar()
volver=input("Regresar a menu (si/no):")
if(volver=="si"):
    Menu()
    Ingresar()
if(volver=="no"):
    exit()
