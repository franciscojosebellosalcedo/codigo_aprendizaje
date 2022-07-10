#include<iostream>
#include<math.h>
using namespace std;


int main(){
    int n;
    cout<<"Ingrese un numero entero: "<<endl;
    cin>>n;
    while((n<=0)){
        cout<<"Numero incorrecto."<<endl;
        cout<<"Ingrese un numero entero: "<<endl;
        cin>>n;

    }
    if((n>0)){
        int total;
        total=0;
        int elevado=0;
        for(int i=1;i<=n;i++){
            elevado=(int)(pow(2,i));
            total=total+(elevado);
        }
        cout<<"El total es de :"<<total;
    }



    return 0;
}