print("¿ Que operacion quiere realizar?")

print("digite 1 para sumar dos numero")
print("digite 2 para restar dos numero")
print("digite 3 para multiplicar dos numero")
print("digite 4 para dividir dos numero")
print("digite 5 para sacar modulo de dos numero")
print("digite 6 para sacar raiz cuadrada de dos numero")
print("digite 7 para sacar la potencia entre dos numero")
print("digite 8 para salir del programa")

menu=0
while(menu <8):
    menu=menu+1
    menu=int(input("ingrese la opcion que desea:"))

    if(menu==1):
        numero1=int(input("digite el primer numero:"))
        numero2=int(input("digite el segundo numero:"))
        suma_numeros=(numero1+numero2)
        print("La suma entre los dos numeros es de:",suma_numeros)

    if(menu==2):
        numero1=int(input("digite el primer numero:"))
        numero2=int(input("digite el segundo numero:"))
        resta_numeros=(numero1-numero2)
        print("La resta entre los dos numeros es de:",resta_numeros)

    if(menu==3):
        numero1=int(input("digite el primer numero:"))
        numero2=int(input("digite el segundo numero:"))
        multi_numeros=(numero1*numero2)
        print("La multiplicacion entre los dos numeros es de:",multi_numeros)

    if(menu==4):
        numero1=int(input("digite el primer numero:"))
        numero2=int(input("digite el segundo numero:"))
        div_numeros=(numero1/numero2)
        print("La divisio entre los dos numeros es de:",div_numeros)

    if(menu==5):
        numero1=int(input("digite el primer numero:"))
        numero2=int(input("digite el segundo numero:"))
        resto_n1=numero1%2
        resto_n2=numero2%2
        print("El modulo del primer numero es de:",resto_n1)

        if(resto_n1==0):
            print("El primer numero es par")
        else:
            print("el primer numero es impar")

        print(" El modulo del segundo numero es de:",resto_n2)

        if(resto_n2==0):
            print("El segundo numero es par")
        else:
            print("el segundo numero es impar")

    if(menu==6):
        import math
        numero1=int(input("digite el primer numero:"))
        numero2=int(input("digite el segundo numero:"))
        raiz_n1=math.sqrt(numero1)
        raiz_n2=math.sqrt(numero2)
        print("La raiz cuadrara del primer numero es de:",raiz_n1)
        print("La raiz cuadrada del segundo numero es de:",raiz_n2)

    if(menu==7):
        numero1=int(input("digite el primer numero:"))
        numero2=int(input("digite el segundo numero:"))
        potencia_numeros=(pow(numero1, numero2))
        print("la potencia entre los numeros es de:",potencia_numeros)







    

    
            
