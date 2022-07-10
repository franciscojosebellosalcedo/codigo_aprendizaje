#include<iostream>
using namespace std;
int main(){
    //Ingrese 1: Agregar saldo.;
    //Ingrese 2: Retirar saldo.;
    //Ingrese 3: Consultar saldo.;
    //Ingrese -1: Salir.;
    int aux;
    double saldoInicial;
    saldoInicial=200.000;
    double agregar=0;
    double retirar=0;
    int opcion;
    double saldo;
    aux=0;
    while ((aux!=-1)){
        string id,menu1,pregunta,menu2;
        menu1="------MENU------\nIngrese 1: Agregar saldo.\nIngrese 2: Retirar saldo.\nIngrese 3: Consultar saldo.\nIngrese -1: Salir.";
        cout<<menu1;
        cout<<"\n";
        cout<<"Ingrese una opcion: ";
        cin>>opcion;
        while((opcion>3)|| (opcion<-1)){
            cout<<"Opcion NO existente.";
            cout<<"Ingrese una opcion nuevamente : ";
            cin>>opcion;
        }
        if((opcion==1)){
            cout<<"Digite su id: ";
            cin>>id;
            while((id.size()<10)){
                cout<<"Error.\nID incorrecto."<<endl;
                cout<<"Digite su ID nuevamente : ";
                cin>>id;
            }
            if((id.size()==10)){
                cout<<"Digite el saldo que desea agregar:";
                cin>>saldo;
            }   
            while((saldo<=0)){
                cout<<"El saldo digitado es incorrecto.\nVuelva a ingresar el saldo nuevamente."<<endl;
                cout<<"Digite el saldo que desea agregar:";
                cin>>saldo;
            }
            if((saldo>0)){
                saldoInicial=saldoInicial+saldo;
                cout<<"USUARIO >>ID: " <<id<<" >>"<< " Nuevo saldo : "<<saldoInicial<<endl;
            }
        }
        if((opcion==2)){
            cout<<"Digite su id: ";
            cin>>id;
            while((id.size()<10)){
                cout<<"Error.\nID incorrecto."<<endl;
                cout<<"Digite su ID nuevamente : ";
                cin>>id;
            }
            if((id.size()==10)){
                cout<<"Ingrese el saldo a retirar: ";
                cin>>saldo;
                while ( (saldo>saldoInicial)||(saldo<=0))
                {
                    cout<<"El saldo digitado es incorrecto."<<endl;
                    cout<<"Digite el saldo que desea retirar nuevamente:"<<endl;
                    cin>>saldo;
                }
                if((saldo>0)&& (saldo<=saldoInicial)){
                    saldoInicial=saldoInicial-saldo;
                    cout<<"Retiraste :"<<saldo<<endl;
                    cout<<"Tu saldo es de: "<<saldoInicial<<endl;
                }
            }               
        }
        if((opcion==3)){
            cout<<"Su saldo Actual es de: "<<saldoInicial<<"\n";
        }
        if((opcion==-1)){
            aux=-1;
            cout<<"programa finalizado.";
        } 
    }
    return 0;
}