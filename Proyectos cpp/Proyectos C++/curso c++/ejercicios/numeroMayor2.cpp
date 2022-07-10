#include<iostream>
using namespace std;
int main(){
    int n1;
    int n2;
    int n3;
    cout<<"Ingrese el primer numero :"<<endl;
    cin>>n1;
    cout<<"Ingrese el segundo numero :"<<endl;
    cin>>n2;
    cout<<"Ingrese el tercer numero :"<<endl;
    cin>>n3;
    if((n1>n2)&& (n1>n3)){
        cout<<"El numero "<<n1<< " es el mayor.";
    }else if((n2>n1)&& (n2>n3)){
        cout<<"El numero "<<n2<< " es el mayor.";
    }else if((n3>n1)&& (n3>n2)){
        cout<<"El numero "<<n3<<" es el mayor.";
    }
    return 0;
}