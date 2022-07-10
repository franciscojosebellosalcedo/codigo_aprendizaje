import os
import time
os.system("cls")
time.sleep(1)

precio=int(input("Ingrese el precio del producto:"))
cantidad_producto=int(input("Ingrese la cantidaa de productos deseados:"))
subtotal=(precio*cantidad_producto)
iva=(subtotal/100)
total=(subtotal+iva)
print("El subtotal de la compra es de:","$",subtotal)
print("El monto del iva es de,","$",iva)
print("El monto total es de:","$",total)
