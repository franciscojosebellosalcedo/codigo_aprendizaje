
aux=0
while(aux!=1):
    def Menu_list():
        print("1: agregar valore a una lista.")
        print("2: borrar valor  de la lista.")
        print("3: actualizar valor de la lista.")
        print('4: Agregar valores nuevos a la lista.')
        print("5: cerra programa.")
        print(" ")
    Menu_list()
    opcion=int(input("Ingrese la opcion :"))
    while (  opcion>5 or opcion==0):
    	print('Error .')
    	opcion=int(input("Ingrese la opcion :"))
    print(" ")
    if (opcion==1):
        array = [ ]
        def Agregar_valor_list():
            
            cantidad_valores=int(input("ingrese la cantidad de valores que va a digitar:"))
            for i in range(0,cantidad_valores):
                valor=int(input(f"digite valor # {i+1} :"))
                array.append(valor)
            print(" ")    
            print("Datos:",array,end=" ")
            print(" ")
        Agregar_valor_list()

    if (opcion==2):
        def Borrar_datos():
            borrar=int(input("Ingrese valor que va a eliminar de la lista:"))
            
            for r in range(len(array)-1,-1,-1):
                if (borrar==array[r]):
                    array.remove(borrar)
            print(array)
        Borrar_datos()
    
    if (opcion==3):
        def Actualizar():
            dato=int(input("Digite el valor que quiere remplazar: "))
            modific=int(input("Digite dato nuevo: "))
            for i in range(len(array)):
                if (dato==array[i]):
                    array[i]=modific
            print(array)

        Actualizar()
    if (opcion==4):
    	def Valores_nuevos():
    		cant=int(input('¿Cuantos datos nuevos va a ingresar : '))	
    		for s in range(cant):
    			valor_nuevo=int(input(f'Ingrese valor nuevo #{ s+1} :'))
    			array.append(valor_nuevo)
    		print(array)
    	Valores_nuevos()
    print(" ")
    if (opcion==5):
    	exit()
    
    aux=int(input("Digite 0 para seguir con el programa \n Digite 1 para cerrar: "))
 


