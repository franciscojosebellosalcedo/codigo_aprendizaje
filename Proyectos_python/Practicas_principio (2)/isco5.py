
"""
print(" algoritmo de mi creatividad")
print(" investigar altura y peso de una persona y decir si es alta o baja y tambien si es pesada o no es tan pesada  ")

altura=float(input(" ingrese altura :"))
peso=int(input(" ingrese peso :"))

formula=(altura+peso)

print("el resultado total de las dos unidades es  :"+str(formula)+str("mts"))

if(formula<10):
    print(" esta persona es muy alta y pesada ")
else:
    print(" esta persona es  baja y no es tan pesada")

# concatenacion de variables

print("Ahora se concatenaran algunos resultados de unas variables")

print(" Resultado de los dos primeros digitos")
vars1=int(input("Ingrese cualquier valor:"))
vars2=int(input("Ingrese cualquier valor:"))

r1=(vars1*vars2)

print("El primer resultado es :"+str(r1))

print(" Resultado de los dos segundos digitos")
vars3=int(input(" Ingrese cualquier valor:"))
vars4=int(input(" Ingrese cualquier valor:"))

r2=(vars3*vars4)

print(" El segundo resultado es :"+str(r2))

print("Datos de los dos resltados:")
print(("Primer resultado=")+str(r1)+"__"+("Segundo resultado=")+str(r2))


print("Ahora se emplearan una entrada de un dato personal")


pronombre=(input("¿ cual es tu pronombre?:"))
print(pronombre)

nombre=(input("¿ cual es tu verdadero nombre?:"))
print(nombre)
"""

# lista en python

print(" numeros en lista.")
numeros=("1","2","4","5","6","7","8","9","10")
for numeros in numeros:
    print("."+ (numeros))
    







