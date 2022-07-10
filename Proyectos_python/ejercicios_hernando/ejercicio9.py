import time
import os
time.sleep(1)
os.system("cls")

numero=int(input("ingrese un numero:"))
resto=numero%2
if(resto==0):
    print("el numero es par")
else:
    print("el numero es impar")    