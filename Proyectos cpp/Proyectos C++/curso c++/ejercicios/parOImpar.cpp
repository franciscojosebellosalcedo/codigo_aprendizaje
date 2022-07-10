#include<iostream>
using namespace std;
int main(){
    int numero=0;
    cout<<"ingrese un numero: ";
    cin>>numero;
    if((numero==0)){
        cout<<"El numero es "<<numero;
    }else if((numero>0)) {
        if((numero%2==0)){
            cout<<"El numero "<<numero<<" es par."<<endl;
        }else {
            cout<<"El numero "<<numero<<" es impar."<<endl;
        }
    }
    

    return 0;
}