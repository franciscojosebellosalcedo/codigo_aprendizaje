#include<iostream>
using namespace std;
int main(){
    double a,b;
    cout<<"Exprecion: a sobre b mas 1";
    cout<<"\nIngrese el valor para a: ";cin>>a;
    cout<<"\nIngrese el valor para b: ";cin>>b;
    double exprecion=0;
    exprecion=(a/b)+1;
    cout.precision(2);
    cout<<"El resultado de la exprecion es: "<<exprecion;
    return 0;
}