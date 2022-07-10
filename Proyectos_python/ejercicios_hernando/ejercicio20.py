lado1=int(input("digite el primer lado del triangulo:"))
lado2=int(input("digite el segundo lado del triangulo:"))
lado3=int(input("digite el tercer lado del triangulo:"))

if((lado1 ==lado2 ==lado3 or lado2==lado3 == lado1) or (lado2 ==lado1 == lado3 or lado3==lado2 == lado1)):
    print(" es un triangulo equilatero")
if( (lado1 ==lado2 !=lado3 or lado2==lado3 !=lado1) or (lado2 ==lado3 !=lado1 or lado1==lado3 !=lado2)):
    print(" es un triangulo isoscele")
if( (lado1 != lado2 !=lado3 and lado2!=lado3 !=lado1) and (lado2 !=lado3 !=lado1 or lado1!=lado3 !=lado2)):
    print(" el triangulo es escaleno")
    
