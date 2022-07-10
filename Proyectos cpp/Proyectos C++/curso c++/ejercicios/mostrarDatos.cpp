#include<iostream>
using namespace std;
int main(){
    int tamanio;
    cout<<"Digite el tamaño de la lista: "<<endl;
    cin>>tamanio;
    int array[tamanio];
    for(int i=0;i<tamanio;i++){
        cout<<"Ingrese el valor de la posicion "<<"["<<(i)<<"] :"<<endl;
        cin>>array[i];
    }
    cout<<"Elementos con sus respectivas posiciones :"<<endl;
    for(int x=0;x<tamanio;x++){
        cout<<"Posicion "<<"["<<(x)<<"]"<<"Elemento: "<<array[x]<<endl;
    }

    return 0;
}