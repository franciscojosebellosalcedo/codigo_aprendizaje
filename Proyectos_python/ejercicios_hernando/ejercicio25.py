recorrido=int(input("ingrese el recorrido durante todo el dia:"))
monto_normal=30000
iva=20
if(recorrido<300):
    monto_pagar=monto_normal
    monto_con_impuesto=(monto_normal*iva)/100
    print("el monto con iva incluido es de:","$",monto_con_impuesto)
    print("el monto a pagar es de:","$",monto_normal)

if( recorrido>300 and recorrido<=1000):
    monto_pagar2=monto_normal+15000
    monto_con_impuesto2=(monto_pagar2*iva)/100
    print("el monto con iva incluido es de:", "$", monto_con_impuesto2)
    print("el monto a pagar es de:", "$", monto_pagar2)

if( recorrido>1000):
    monto_pagar3=monto_normal+10000
    monto_con_impuesto3=(monto_pagar3*iva)/100
    print("el monto con iva incluido es de:", "$", monto_con_impuesto3)
    print("el monto a pagar es de:", "$", monto_pagar3)

