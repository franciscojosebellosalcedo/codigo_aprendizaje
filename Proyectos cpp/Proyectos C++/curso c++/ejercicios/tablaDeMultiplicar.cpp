#include<iostream>
using namespace std;
int main(){
    int aux;
    aux=0;
    while((aux!=-1)){
        int numero;
        cout<<"----------TABLA DE MULTIPLICACION----------"<<endl;
        cout<<"Digite el numero para saber su tabla de multiplicacion: ";cin>>numero;
        while((numero<0)){
            cout<<"Numero incorrecto."<<endl;
            cout<<"Digite nuevamente el numero para saber su tabla de multiplicacion: ";cin>>numero;

        }
        if((numero>0)){
            cout<<"TABLA DEL NUMERO "<<numero<<endl;
            for(int i=1;i<=10;i++){
                cout<<numero<<" X "<<(i)<<" = "<<(numero*i)<<endl;
            }
        }
        cout<<"¿ Desea seguir con el programa?."<<endl;
        cout<<"Ingrese 1: Seguir.\nIngrese -1: Salir."<<endl;
        cout<<"Ingrese una opcion: "<<endl;
        cin>>aux;
    }  

    return 0;
}