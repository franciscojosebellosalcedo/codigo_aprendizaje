import os
import time
time.sleep(1)
os.system("cls")

def multi(lista):
    print(lista)
    multiplicacion = 2
    for i in lista:
        mult = multiplicacion*i

        print("multiplicado", mult)

multi([3, 4, 1, 2, 5])
