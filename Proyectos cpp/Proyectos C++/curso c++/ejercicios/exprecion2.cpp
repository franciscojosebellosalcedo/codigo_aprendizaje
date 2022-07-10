#include<iostream>
using namespace std;
int main(){
    double a,b,c,d;
    cout<<"Exprecion: a+b sobre a+c"<<endl;
    cout<<"Ingrese el valor para a: ";cin>>a;
    cout<<"Ingrese el valor para b: ";cin>>b;
    cout<<"Ingrese el valor para c: ";cin>>c;
    cout<<"Ingrese el valor para d: ";cin>>d;
    double exprecion=0;
    exprecion=(a+b)/(c/d);
    cout.precision(2);
    cout<<"El resultado de la exprecion es : "<<exprecion;
    return 0;
}