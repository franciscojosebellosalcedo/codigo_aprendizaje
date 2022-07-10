#include<iostream>
using namespace std;
int main(){
    cout<<"Exprecion : a+ b/c / d+ e/f "<<endl;
    double  a,b,c,d,e,f;
    double primeraParte=0;
    double segundaParte=0;
    cout<<"Ingrese el valor para a: ";cin>>a;
    cout<<"Ingrese el valor para b: ";cin>>b;
    cout<<"Ingrese el valor para c: ";cin>>c;
    cout<<"Ingrese el valor para d: ";cin>>d;
    cout<<"Ingrese el valor para e: ";cin>>e;
    cout<<"Ingrese el valor para f: ";cin>>f;
    primeraParte=a+(b/c);
    segundaParte=d+(e/f);
    double resultado=0;
    cout.precision(2);
    resultado=primeraParte/segundaParte;
    cout<<"El resultado es: "<< resultado;
    
    return 0;
}