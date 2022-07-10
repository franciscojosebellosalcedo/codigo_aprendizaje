import os
import time
os.system("cls")
time.sleep(1)

descuento=15
total=int(input("Ingrese el total de su compra:"))
total_pago=(total*descuento)/100
print("El total de su comopra incluyendo el descuento de 15% es de:","$",total_pago)