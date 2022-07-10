#include<iostream>
using namespace std;
int main(){
    int numero;
    numero=1;
    int numeros;
    numeros=0;
    int numerosNegativos;
    numerosNegativos=0;
    while((numero!=0)){
        cout<<"Ingrese un numero: ";
        cin>>numero;
        while((numero<0)){
            cout<<"Ingrese el numero nuevamente: ";
            cin>>numero;
            numerosNegativos=numerosNegativos+1;
        }
        numeros=numeros+1;
    }
    cout<<"Cantidad de numeros negativos ingresados: "<<numerosNegativos<<endl;
    cout<<"Cantidad de numeros ingresados: "<<numeros<<endl;


    return 0;
}