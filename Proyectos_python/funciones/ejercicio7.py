import time
import os
time.sleep(1)
os.system("cls")

def Inicio_sesion():
    aux = 0
    while(aux < 3):
        print("Solo tenemos tres intentos para iniciar sesion.")
        aux = aux+1
        nombre_usuario = "usuario1"
        contaseña_usuario = "asdasd"
        nombre = input("Ingrese su nombre:")
        contraseña = input("Ingrese contraseña:")
        if (nombre == nombre_usuario and contraseña == contaseña_usuario):
            print("Has iniciado sesion")
            exit()
        else:
            print("ERROR", aux)
    print("\n")
    print("Intentos fallidos", aux)
    print("Intentelo mas tarde")

Inicio_sesion()







# def Login(nombre, contaseña):
#     nombre_usuario = "usuario1"
#     contaseña_usuario = "asdasd"
#     print(" ")
#     if (nombre == nombre_usuario and contaseña == contaseña_usuario):
#         print("Has iniciado sesion")
#         exit()
#     else:
#         print("ERROR DE INICIO SESION.")
#     print("\n")

# Login("usuario1","asdasd" )
            

