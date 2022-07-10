def numero_primo():
	aux=0
	contador=0
	while (   aux!=1 ):
		numero=int(input('ingrese un numero :'))
		while(numero<=0):
			print(  "El numero " +str(numero)+" es incorrecto")
			numero=int(input('Ingrese un numero positivo: '))
		if(numero>1):
			for i in range(2,numero):
				resto=numero%i
				print(numero ,"%",(i),'=' ,resto)
				if(resto==0):
					contador=contador+1
			if(contador==0):
				print('El numero ',numero,' es primo')
			else:
				print("El numero ",numero,'no es primo')			
		aux=int(input('seguir 0\nCerrar 1: '))
		while((aux<0) or (aux>1)):
			print("Error. Opcion incorrecta.")
			aux=int(input('seguir 0\nCerrar 1: '))
	print("Programa finalizado")
numero_primo()
		