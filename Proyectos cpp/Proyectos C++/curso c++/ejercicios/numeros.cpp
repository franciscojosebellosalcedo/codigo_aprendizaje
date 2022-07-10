#include <iostream>
using namespace std;
int main(){
    int numero1,numero2,numero3,numero4;
    cout<<"Ingrese tres numeros :";
    cin>>numero1;
    cin>>numero2;
    cin>>numero3;
    cout<<"Ingrese el cuarto numero :";
    cin>>numero4;
    if((numero4==numero1)){
        cout<<"El numero "<<numero4<<" coinside con el primer numero.";
    }else if((numero4==numero2)){
        cout<<"El numero "<<numero4<<" coinside con el segundo numero.";
    }else if((numero4==numero3)){
        cout<<"El numero "<<numero4<<" coinside con el tercer numero." ;
    }else{
        cout<<"El numero "<<numero4<< " no coinside con ninguno";
    }

    return 0;
}