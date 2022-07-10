#include<iostream>
#include<math.h>
using namespace std;
int main(){
    int aux;
    aux=0;
    int contador;
    contador=0;
    int numero=0;
    while((aux!=1)){
        cout<<"Digite un numero entre 1 y 100 : "<<endl;
        cin>>numero;
        while((numero<=0)||(numero>100)){
            cout<<"Numero incorrecto."<<endl;
            cout<<"Digite un numero entre 1 y 100 nuevamente : "<<endl;
            cin>>numero;
        }
        if((numero>=1)&&(numero<=100)){
            int numeroAle;
            numeroAle =1+rand()%(10);
            if((numeroAle>numero)){
                cout<<"El numero es mayor."<<endl;
                aux=0;
                contador=contador+1;
                
            }else if((numeroAle<numero)){
                cout<<"El numero es menor."<<endl;
                aux=0;
                contador=contador+1;
            }
           
            if((numero==numeroAle)){
                cout<<"Numero adivinado."<<endl;
                aux=1;  
             }     
        }
     
    }
    cout<<"Cantidad de intentos: "<<contador<<endl;


    return 0;
}