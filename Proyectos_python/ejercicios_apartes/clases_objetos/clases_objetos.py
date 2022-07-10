import time,os
os.system("cls")
time.sleep(1)

""" CLASES Y OBJETOS I"""
# class Auto:
#     marca="mazda "
#     modelo=2004
#     placa="BZ 123"

# taxi=Auto()
# print(taxi.marca)
# print(taxi.modelo)

""" CLASES Y OBJETOS II"""
# class Jugadores_A:
#     j1="marcelo"
#     j2="messi"
#     j3="james"

# class jugadores_B:
#     j1="neymar"
#     j2="falcao"
#     j3=12*12

# print(Jugadores_A.j1)

""" CLASES Y OBJETOS III"""

# class Jugador:
#     pass


# play1 = Jugador()

# """objeto.atributo=valor"""

# play1.vida=500
# play1.resistencia=100
# play1.arma="m 60"
# play1.xp=10

# class Enemigo:
#     pass

# villano=Enemigo()

# """objeto.atributo=valor"""

# villano.vida=100
# villano.resistencia=50
# villano.arma="pistola"
# villano.xp=5

# print(play1.vida)


""" CLASES Y OBJETOS (DEF)"""

# class Matematicas:
#     def division(self):
#         self.n1=12
#         self.n2=12

# resultado=Matematicas()
# resultado.division()
# total=(resultado.n1/resultado.n2)
# print(total)

""" CLASES Y OBJETOS (DEF)  (__init__)"""

# class Matematicas:
#     def __init__(self):
#         self.n1=12
#         self.n2=12
# suma=Matematicas()
# print(suma.n1+suma.n2)




# class Matematicas:
#     def resta(numeros):
#         numeros.num1=int(input("ingrese el primer numero:"))
#         numeros.num2 = int(input("ingrese el sugundo numero:"))
#     def suma(self):
#         self.num1 = int(input("ingrese el primer numero:"))
#         self.num2 = int(input("ingrese el segundo numero:"))

# resultado_suma = Matematicas()
# resultado_suma.suma()
# total_suma = (resultado_suma.num1+resultado_suma.num2)
# print("La suma de los dos valores es de:",total_suma)

# resultado_resta=Matematicas()
# resultado_resta.resta()
# total_resta = (resultado_resta.num1-resultado_resta.num2)
# print("La resta de los dos valores es de:",total_resta)





def calculos_matematicos(n1,s,n2):
    if (s== "+"):
        suma_numeros=n1+n2
        print("La suma de los dos numeros es :",suma_numeros)
    if(s=="-"):
        resta_numeros=n1-n2
        print("La resta de los dos numeros es :",resta_numeros)
    if (s == "*"):
        multi_numeros = n1*n2
        print("La multiplicacion de los dos numeros es :", multi_numeros)
    if(s == "/"):
        div_numeros = n1/n2
        print("La division de los dos numeros es:", div_numeros)

calculos_matematicos(2, "+", 3)






























        
        






    
    


    






















