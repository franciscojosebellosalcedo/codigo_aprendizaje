#include<iostream>
using namespace std;
int main(){
    char array[5];
    for(int i=0;i<5;i++){
        cout<<"Ingrese el valor de la posicion "<<"["<<(i)<<"] :"<<endl;
        cin>>array[i];
    }
    cout<<"Valores :"<<endl;
     for(int z=0;z<5;z++){
        cout<<array[z]<<" ";
    }

    return 0;
}