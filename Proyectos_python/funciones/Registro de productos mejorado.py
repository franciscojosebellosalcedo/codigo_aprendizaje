from os import system
from time import sleep
tienda=[]
def menu():
    system('cls')
    print("\033[4;35m"+"--------TIENDA LOS TIFONES--------\n"+'\033[0;m')
    print("[1].Ingresar Productos")
    print("[2].Visualizar Productos")
    print("[3].Actualizar Productos")
    opcion=int(input("Seleccione Alguna Opcion: "))
    while opcion>3 or opcion<1:
        print("ERROR")
        sleep(1)
        system('cls')
        print("\033[4;35m"+"--------TIENDA LOS TIFONES--------\n"+'\033[0;m')
        print("1.Ingresar Productos: ")
        print("2.Visualizar Productos: ")
        opcion=int(input("Ingrese La Opcion: "))
    if opcion==1:
        ingresar_datos(0,0)
    elif opcion==2:
        mostrar_productos()
    elif opcion==3:
        actualizar_productos()
def finalizar_ingreso(info,identproduct):
    if len(info)==0:
        ingresar_datos(0,identproduct)
    elif info=="0":
        menu()
    else:
        print("ERROR")
        exit()
def ingresar_datos(dato,identproduct):
    system('cls')
    print("\033[7;33m"+"------------DATOS_PRODUCTO------------"+'\033[0;m')
    while dato==0:
        identproduct=identproduct+1
        print(f"Producto Numero {identproduct}")
        nombre=str(input("Escriba el nombre del producto: "))
        nombremay=nombre.capitalize()
        cantidad=int(input("Ingrese la cantidad del producto: "))
        precio_unidad=float(input("ingrese el precio de la unidad: $"))
        unidad_de_medida=str(input("ingrese la unidad de medidad: "))
        referencia=str(input("ingrese la referencia: "))
        referenciamay=referencia.capitalize()
        fechaingreso=str(input("Fecha de ingreso: "))
        fechavencimiento=str(input("Fecha de vencimiento: "))
        tienda.append([nombremay,cantidad,precio_unidad,unidad_de_medida,referenciamay,fechaingreso,fechavencimiento])
        print("Presione ENTER Para continuar ingresando productos")
        print("Ingrese 0 para volver al menu")
        ingropcion=str(input(""))
        finalizar_ingreso(ingropcion,identproduct)
def mostrar_productos():
    system('cls')
    if len(tienda)==0:
        print("LA LISTA DE PRODUCTOS ESTA VACIA")
        sleep(2)
        menu()
    else:
        system('cls')
        print("\033[7;34m"+"------------BASE_DE_DATOS_PRODUCTOS------------"+'\033[0;m')
        for i in range(len(tienda)):
            print(f"Producto Numero {i+1}")
            print("Nombre de Producto:",tienda[i][0],"\nCantidad:",tienda[i][1],"\nPrecio unidad:",tienda[i][2],"\nUnidad de medidad:",tienda[i][3],"\nReferencia:",tienda[i][4],"\nFecha de ingreso:",tienda[i][5],"\nFecha de Vencimiento:",tienda[i][6])
            print("------------------------------------")
        volver_menu=int(input("Quieres volver al menu(Ingrese 0 para volver al menu): "))
        if volver_menu==0:
            menu()
        else:
            print("Error de volver: ")
            exit()
def actualizar_productos():
    system('cls')
    if len(tienda)==0:
        print("LA LISTA DE PRODUCTOS ESTA VACIA")
        sleep(1)
        menu()
    else:
        print("\033[7;32m"+"-----------ACTUALIZAR PRODUCTO-----------"+'\033[0;m')
        Nombred=str(input("Ingresar el nombre del producto: "))
        Nombre=Nombred.capitalize()
        Referenciad=str(input("Ingresar la referencia del producto: "))
        Referencia=Referenciad.capitalize()
        print("")
        for ind in range(len(tienda)):
            if Nombre==tienda[ind][0] and Referencia==tienda[ind][4]:
                while True==True:
                    system('cls')
                    print("\033[7;32m"+"-----------ACTUALIZAR PRODUCTO-----------"+'\033[0;m')
                    print("1.Nombre de Producto:",tienda[ind][0],"\n2.Cantidad:",tienda[ind][1],"\n3.Precio unidad:$",tienda[ind][2],"\n4.Unidad de medidad:",tienda[ind][3],"\n5.Referencia:",tienda[ind][4],"\n6.Fecha de ingreso:",tienda[ind][5],"\n7.Fecha de Vencimiento:",tienda[ind][6],"\n0.Para regresar al menu")
                    opcion=int(input("Seleccione la Opcion para actualizar: "))
                    if opcion==1:
                        nuevomay=str(input("Ingrese el nuevo nombre del producto: "))
                        nuevo=nuevomay.capitalize()
                        tienda[ind][0]=nuevo 
                    elif opcion==2:
                        nuevo=int(input("Ingresar la nueva cantidad: "))
                        tienda[ind][1]=nuevo
                    elif opcion==3:
                        nuevo=float(input("Ingresar el nuevo precio de la unidad: "))
                        tienda[ind][2]=nuevo
                    elif opcion==4:
                        nuevomay=str(input("Ingresar la nueva unidad de medida: "))
                        nuevo=nuevomay.capitalize()
                        tienda[ind][3]=nuevo
                    elif opcion==5:
                        nuevo=str(input("Ingresar la nueva referencia: "))
                        tienda[ind][4]=nuevo
                    elif opcion==6:
                        nuevo=str(input("Ingresar la nueva fecha de ingreso: "))
                        tienda[ind][5]=nuevo
                    elif opcion==7:
                        nuevo=str(input("Ingresar la nueva fecha de vencimiento: "))
                        tienda[ind][6]=nuevo
                    elif opcion==0:
                        menu()
                    else:
                        print("Error")
        system('cls')
        print("NO SE ENCONTRO NINGUN DATO")
        sleep(2)
        menu()           
menu()