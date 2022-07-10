#include<iostream>
using namespace std;

int main(){
    int v;
    v=0; 
    int suma;
    suma=0;
    int n=1;
    while((v<3)){
        
        int numero;
        n=n+2;
        numero=n;
        cout<<1<<endl;
        cout<<numero<<endl;
        suma=suma+numero;
        v=v+1;
    }
    cout<<"suma :"<<suma+1<<endl;


    return 0;    
}