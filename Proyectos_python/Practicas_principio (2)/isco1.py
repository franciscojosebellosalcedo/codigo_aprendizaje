a=int(input("ingrese  numero a:"))
b=int(input("ingrese numero b:"))
c=int(input("ingrese numero c:"))

if(a>b and c):
    print("a es mayor ")
else:
    print("a es menor")
if(b>a and c):
    print("b es mayor")
else:
    print("b es menor")
if(c>a and b):
    print("c es mayor")
else:
    print("c es menor")

print(" correccion de valores en caso de que sean iguales ")

if(a==b and c):
    print(" a es un valor incorrecto")
if(b==a and c):
    print(" b es un valor incorrecto")
if(c==a and b):
    print("c es un valor incorrecto")
    

