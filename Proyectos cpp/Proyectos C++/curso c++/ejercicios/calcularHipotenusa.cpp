#include<iostream>
using namespace std;
int main(){
    cout<<"Calculo de hipotenusa de un triangulo rectangulo"<<endl;
    double cateto1,cateto2;
    cout<<"Ingrese el valor del primer cateto: ";
    cin>>cateto1;
    cout<<"Ingrese el valor del segundo cateto: ";
    cin>>cateto2;
    double resultado=0;
    resultado=cateto1+cateto2;
    cout<<"La hipotenusa del triangulo rectangulo tiene un valor de: "<<resultado;

    return 0;
}