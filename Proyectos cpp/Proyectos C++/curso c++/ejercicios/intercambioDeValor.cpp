#include<iostream>
using namespace std;
int main(){
    int a,b;
    cout<<"Ingrese el valor para a: ";cin>>a;
    cout<<"Ingrese el valor para b: ";cin>>b;
    int intercambio1=a;
    int intercambio2=b;
    a=intercambio2;
    b=intercambio1;
   
    cout<<"Valor de a: "<<a<<endl;
    cout<<"Valor de b: "<<b<<endl;

    return 0;
}