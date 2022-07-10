import time
import os
time.sleep(1)
os.system("cls")

def Factorial_numero(numero):
    if(numero!=0):
        f=1
        for i in range(1,numero+1):
            f=f*i
        print("El factorial de ",numero,"es",f)

Factorial_numero(6)



