radio=float(input("ingrese el radio del cilindro:"))
altura=float(input("ingrese la altura del cilindro:"))

pi=3.1416
area=(2*pi*radio)+(radio+altura)
print("el area del cilindro es de:",area)
volum=(pi*radio**2)*(altura)
print("el volumen del cilindro es de:",volum)
