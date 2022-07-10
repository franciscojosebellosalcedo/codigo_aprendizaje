#include<iostream>
#include<math.h>
using namespace std;
int main(){
    int opcion;
    cout<<"Ingrese 1: Cubo de un numero.\nIngrese 2: Numero par o impar\nIngrese 3: Salir. "<<endl;
    cout<<"Digite una opcion: ";
    cin>>opcion;
    while((opcion>3)|| (opcion<=0)){
        cout<<"Opcion no valida."<<endl;
        cout<<"Digite una opcion nuevamente: "<<endl;
        cin>>opcion;
    }
    if((opcion>=1)&&(opcion<=3)){
        if((opcion==1)){
            int numero;
            cout<<"Ingrese un numero entero: "<<endl;
            cin>>numero;
            while ((numero<=0))
            {
               cout<<"Numero incorrecto."<<endl;
               cout<<"Ingrese un numero entero nuevamente: "<<endl;
                cin>>numero;
            }
            if((numero>0)){
                int cubo;
                cubo=(int)(pow(numero,3));
                cout<<"El cubo del numero "<<numero<<" es "<<cubo;
            }
            
        }
        if((opcion==2)){
            int opcion2;
            cout<<"Sabremos si un numero es par o impar.\n";
            cout<<"Puede ingresar"<<endl;
            
            cout<<"Ingrese una opcion: ";
            cin>>opcion2;
            while((opcion2<1)||(opcion2>3)){
                cout<<"Opcion incorrecta."<<endl;
                cout<<"Ingrese una opcion nuevamente: "<<endl;
                cin>>opcion2;

            }
            if((opcion2>=1)&&(opcion2<=3)){
                if((opcion2==1)){
                    int numero;
                    cout<<"Ingrese un numero entero: "<<endl;
                    cin>>numero;
                    while((numero<=0)){
                        cout<<"Numero no valido."<<endl;
                        cout<<"Ingrese un numero entero nuevamente: "<<endl;
                        cin>>numero; 
                    }
                    if((numero>0)){
                        if((numero%2==0)){
                            cout<<"El numero "<<numero<<" es par."<<endl;

                        }else{
                            cout<<"El numero "<<numero<<" es impar."<<endl;
                        }
                    }
                }
            }
            
        }
        if((opcion==3)){
            cout<<"Programa finalizado."<<endl;
        }
    }


    return 0;
}