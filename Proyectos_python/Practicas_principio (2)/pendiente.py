def Funcion1():
	horas=int(input('Ingrese horas:'))
	conversion1=(horas*3600)/1
	print(horas,"horas convertido a segundo son :",conversion1," segundos")
	minutos=int(input('Ingrese minutos:'))
	conversion2=(minutos*60)/1
	print(minutos," minutos convertidos a segundos son:",conversion2,"segundos")
	
Funcion1()

def Funcion2():
	segundos=int(input("Ingrese la cantidad de segundos:"))
	conversion1=segundos/3600
	print(segundos," segundos convertidos a horas son:",conversion1," horas")
	segundos=int(input("Ingrese la cantidad de segundos:"))
	conversion2=segundos/60
	print(segundos,"segundos convertidos a minutos son:",conversion2,"minutos")
	
Funcion2()

