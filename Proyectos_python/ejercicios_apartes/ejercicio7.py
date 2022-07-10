cantidad_kilometros=int(input(" Ingrese la cantidad de kilometros a recorrer:"))
precio_combustible=int(input("Ingrese el precio de un litro de combustible:"))
precio_peaje=int(input("ingrese el precio del peaje:"))
monto_combustible=(precio_combustible*13)/100
monto_peaje=precio_peaje*2
total=monto_combustible+monto_peaje
print("el total de dinero necesitado es de:","$",total)