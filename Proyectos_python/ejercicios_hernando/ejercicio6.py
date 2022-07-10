a=int(input("ingrese un valorA:"))
b=int(input("ingrese un valorB diferente al anterior:"))
c=int(input("ingrese un valorC diferente a los anteriores (A y B):"))


if(a<b and a<c):
    print(" el valorA es el menor")
if(b<a and b<c):
    print("el valorB es el menor")
if(c<a and c<b):
    print("el valorC es el menor")
