#include<iostream>
using namespace std;
int main(){
        int valor;
        cout<<"Ingrese un valor numerico:";
        cin>>valor;
        while((valor>2) || (valor<=0)){
            cout<<"Valor no correcto";
            cout<<"Ingrese un valor numerico nuevamente:";
            cin>>valor;
        }
        switch (valor)
        {
        case 1:
            int primerNumero;
            int segundoNumero;
            cout<<"ingrese el primer numero :"<<endl;
            cin>>primerNumero;
            cout<<"ingrese el segundo numero :"<<endl;
            cin>>segundoNumero;
            int suma;
            suma=(primerNumero+segundoNumero);
            cout<<"Resultado es: "<<suma;
            break;
        case 2:
            cout<<"Hola "<<"Francisco";
            break;
        default:
            cout<<"fin programa";
            break;
        }
    return 0;
}