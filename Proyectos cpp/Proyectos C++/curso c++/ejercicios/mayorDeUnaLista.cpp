#include<iostream>
using namespace std;
int main(){
    int numeros;
    cout<<"Ingrese el numero de la  cantidad de elementos: "<<endl;
    cin>>numeros;
    int array[numeros];
    for(int i=0;i<numeros;i++){
        cout<<"Digite el valor de la posicion "<<"["<<(i)<<"] :"<<endl;
        cin>>array[i];
    }
    cout<<"Elementos :"<<endl;
    for(int i=0;i<numeros;i++){
        cout<<array[i]<<" "<<endl;
    }
    int mayor=array[0];
    for(int x=0;x<numeros;x++){
        if((array[x]>mayor)){
            mayor=array[x];
        }
    }cout<<"El mayor es :"<<mayor;


    return 0;
}