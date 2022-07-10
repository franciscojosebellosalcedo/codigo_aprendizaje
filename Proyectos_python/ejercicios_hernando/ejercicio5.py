

a = int(input("ingrese un valorA:"))
b = int(input("ingrese un valorB:"))
c = int(input("ingrese un valorC:"))

if(a > b and a > c):
    print(" el valor A es el mayor")
if(b > a and b > c):
    print("el valor B es el mayor")
if(c > a and c > b):
    print("el valor C es el mayor")


if((a == b and a != c or a == c and a != b) or 
    (b == a and b != c or b == c and b != a) or 
    (c == a and c != b or c == b and c != a or 
    (a == b and a == c or b == a and b == c or c == a and c == b))):
    print(" ¡ERROR! Hay valores iguales , tienen que ser valores diferentes")
