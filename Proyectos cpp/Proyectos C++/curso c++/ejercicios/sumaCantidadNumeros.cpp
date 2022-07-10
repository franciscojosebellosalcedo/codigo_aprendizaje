#include<iostream>
using namespace std;
int main(){
    int cantidadNumeros1;
    int cantidadNumerosPares1=0;
    int cantidadNumerosImpares1=0;
    int numero1;
    int suma1=0;
    cout<<"Digite la cantidad de numeros enteros que va a sumar: ";
    cin >> cantidadNumeros1;
    for (int i = 0; i < cantidadNumeros1;i++)
    {
        cout<<"Ingrese numero #:"<<i+1<<":";
        cin>>numero1;
        if(numero1%2==0){
            cantidadNumerosPares1+=1;
        }
        else{
            cantidadNumerosImpares1+=1;
        }
        while(numero1<=0){
            cout<<"El numero "<<numero1<<" es negativo.\nIngrese un numero positivo.";
            cout<<"\nIngrese numero #:"<<i+1<<" positivo :";
            cin>>numero1;
        }
        suma1=suma1+ numero1;
    }
    cout<<"La suma total de los numeros enteros es: "<<suma1;
    cout<<"\nCantidad de numeros pares ingresados: "<<cantidadNumerosPares1;
    cout<<"\nCantidad de numeros impares ingresados: "<<cantidadNumerosImpares1;
    if(suma1%2==0){
        cout<<"\nEl resultado "<<suma1<<" es par.";
    }else{
        cout<<"\nEl resultado "<<suma1<<" es impar";
    }
        return 0;
}