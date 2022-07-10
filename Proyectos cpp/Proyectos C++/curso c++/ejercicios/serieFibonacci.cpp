#include<iostream>
using namespace std;
int main(){
    int numero;
    cout<<"Ingrese un numero: ";cin>>numero;
    if((numero>0)){
        int z=1,y=1,x=0;
        int aux=0;
        cout<<"Serie Fibonacci:"<<endl;
        cout<<1<<endl;
        while(aux<numero){
            z=x+y;
            cout<<z<<endl;//1 
            x=y;//1 
            y=z;
            
            
           aux=aux+1;
        }

    }else{
        cout<<numero;
    }

    return 0;
}