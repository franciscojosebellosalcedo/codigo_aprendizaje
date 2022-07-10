import time
import os
time.sleep(1)
os.system("cls")


def ConvertirEspacio(texto):
    for i in range(len(texto)):
        print(texto[i],end=" ")

ConvertirEspacio("hola, mundo")