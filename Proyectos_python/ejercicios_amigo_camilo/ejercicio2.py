import time
import os
time.sleep(1)
os.system("cls")


nombre_trabajador=input("ingrese el nombre del trabajador:")
cedula=int(input("ingrese su numero de documento:"))
salario_basico=300000
maxi_dias_laborales=30
salario_mini_legal_vige=589500

dias_laborados=int(input("ingrese las horas trabajadas: "))
if (dias_laborados<30):
    sueldo_devegando=salario_basico*dias_laborados
    if(salario_basico<salario_mini_legal_vige):
        auxilio_transporte=(70500*dias_laborados)/maxi_dias_laborales
        total_ventas_mes=int(input("ingrese el total de las ventas durante el mes:"))
        comision_venta=total_ventas_mes*2
        total_devegando=sueldo_devegando+comision_venta
        pregunta=input("¿Hizo un tipo de prestamo? (si/no):")
        if (pregunta=="si"):
            prestamo=int(input("digite el valor del prestamo:"))
            total_salario=total_devegando-prestamo
print("\n")
print("Cedula del trabajador:",cedula)
print("Nombre del trabajador:",nombre_trabajador)
print("Salario basico:","$",salario_basico)
print("Auxilio de tranporte:","$",auxilio_transporte)
print("Comision de venta:","$",comision_venta)
print("Prestamo:","$",prestamo)
print("Salario total a recibir:","$",total_salario)

