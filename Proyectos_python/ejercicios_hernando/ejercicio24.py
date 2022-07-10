
descuento1=10
descuento2=15

obs=0

while(obs<5):
    print("______________________________________________________________")
    print("por la compra de 3 o mas docenas se le obsequia un producto")
    cantidad_docenas = int(
            input("ingrese la cantidad de docenas que quiere comprar:"))
    valor_docena = int(input("ingrese el valor de las docenas:"))
    if(cantidad_docenas<3):
        print("El monto de comprar:","$",valor_docena)
        monto_descuento1=(valor_docena*descuento1)/100
        print("El monto del descuento es de:","$",monto_descuento1)
        monto_a_pagar1=(valor_docena-monto_descuento1)
        print("El monto a pagar es de:","$",monto_a_pagar1)

    elif(cantidad_docenas>=3):
        obs=obs+1
        print("El monto de comprar:", "$", valor_docena)
        monto_descuento2 = (valor_docena*descuento2)/100
        print("El monto del descuento es de:", "$", monto_descuento2)
        monto_a_pagar2 = (valor_docena-monto_descuento2)
        print("El monto a pagar es de:", "$", monto_a_pagar2)
print("La cantidad de productos obsequiados fueron:",obs)
















    



    



