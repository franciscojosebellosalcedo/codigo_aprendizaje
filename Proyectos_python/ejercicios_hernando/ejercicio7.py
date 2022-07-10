numero1=int(input("ingrese el primer numero:"))
numero2=int(input("ingrese el segundo numero:"))
numero3=int(input("ingrese el tercer numero:"))
numero4=int(input("ingrese el cuarto numero:"))

if(numero1>numero2 and numero1>numero3 and numero1>numero4):
    print("el primer numero es el mayor")

if(numero2 > numero1 and numero2 > numero3 and numero2 > numero4):
    print("el segundo numero es el mayor")

if(numero3 > numero1 and numero3 > numero2 and numero3 > numero4):
    print("el tercer numero es el mayor")

if(numero4 > numero1 and numero4 > numero2 and numero4 > numero3):
    print("el cuarto numero es el mayor")


if(numero1 < numero2 and numero1 < numero3 and numero1 < numero4):
    print("el primer numero es el menor")

if(numero2 < numero1 and numero2 < numero3 and numero2 < numero4):
    print("el segundo numero es el menor")

if(numero3 < numero1 and numero3 < numero2 and numero3 < numero4):
    print("el tercer numero es el menor")

if(numero4 < numero1 and numero4 < numero2 and numero4 < numero3):
    print("el cuarto numero es el menor")
