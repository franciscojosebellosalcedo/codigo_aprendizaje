#include<iostream>
using namespace std;
int main(){
    cout<<"Exprecion: a+ b/ c-d"<<endl;
    double a,b,c,d;
    double resultado=0;
    cout<<"Ingrese el valor para a: ";cin>>a;
    cout<<"Ingrese el valor para b: ";cin>>b;
    cout<<"Ingrese el valor para c: ";cin>>c;
    cout<<"Ingrese el valor para d: ";cin>>d;
    resultado=a+(b/c-d);
    cout.precision(2);
    cout<<"El resultado de la exprecion es: "<<resultado;


    return 0;
}