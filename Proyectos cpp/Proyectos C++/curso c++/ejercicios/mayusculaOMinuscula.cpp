#include<iostream>
using namespace std;
int main(){
    char letra;
    cout<<"Ingrese una letra: ";
    cin>>letra;
    if((islower(letra))){
        cout<<"La letra es minuscula.";
    }else if((isupper(letra))){
        cout<<"La letra es mayuscula.";
    }
    return 0;
}