#include <iostream>
using namespace std;
int main(){
    int edad;
    cout<<"Ingrese su edad: ";
    cin>>edad;
    while((edad<=0)|| (edad>=180)){
        cout<<"Error de edad.";
        cout<<"Ingrese su edad nuevamente : ";
        cin>>edad;
    }
    if((edad>18)&&(edad<25)){
        cout<<" Tu edad esta en el rango de 18-25 años.";

    }else{
        cout<<" Tu edad no esta en el rango de 18-25 años.";
    }

    return 0;
}