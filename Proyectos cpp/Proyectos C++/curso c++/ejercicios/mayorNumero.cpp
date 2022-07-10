#include<iostream>
using namespace std;
int main(){
    int n1;
    int n2;
    cout<<"Ingrese el primer numero :"<<endl;
    cin>>n1;
    cout<<"Ingrese el segundo numero :"<<endl;
    cin>>n2;
    if((n1>n2)){
        cout<<"El numero "<<n1<< " es el mayor.";
    }else if((n2>n1)){
        cout<<"El numero "<<n2<< " es el mayor.";
    }
    else if((n1==n2) || (n2==n1)){
        cout<<"El numero "<<n1<< " y "<< n2<<" son iguales.";
    }
    return 0;
}