#include<iostream>
using namespace std;

int main(){
    string nombre;
    string apellido;
    int edad;
    double estatura;

    cout << "Ingrese su edad: ";
    cin >> edad;
    cout << "Ingrese su estatura: ";
    cin >> estatura;
    cout<<"Ingrese su nombre: ";
    cin>>nombre;
    cout<<"Ingrese su apellido: ";
    cin>>apellido;
    
    cout<<"\nNombre: "<<nombre;
    cout<<"\nApellido: "<<apellido;
    cout<<"\nEdad: "<<edad;
    cout<<"\nEstatura: "<<estatura;
    if(edad<18){
        cout<<"\n"<<nombre<<" eres menor de edad."<<endl;
    }else{
        cout<<"\n"<<nombre<<" eres mayor de edad."<<endl;
    }
    if(estatura>=1.70){
        cout<<nombre<<" eres muy alto"<<endl;
    }else{
        cout<<nombre<<" eres muy bajo"<<endl;
    }

    return 0;
}