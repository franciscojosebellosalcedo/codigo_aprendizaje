#include<iostream>
using namespace std;

int main(){   
    system("cls");
    
    int tamanio=0;
    cout<<"Ingrese el numero de la cantidad de elementos que tendra la lista: ";
    cin>>tamanio;
    int array [tamanio];
    for(int i=0;i<tamanio;i++){
        cout<<"Ingrese el valor de la posicion "<<i<<":";
        cin>>array[i];
    }
    for(int x=0;x<tamanio;x++){
        cout << "\nIndice: " << (x) << " Valor: " << array[x];
    }
    int mayor=array[0];
    for(int z=0;z<tamanio;z++){
        if(array[z]>mayor){
            mayor=array[z];
        }
    }
    int menor = array[0];
    for (int r = 0; r < tamanio; r++)
    {
        if (array[r] < menor)
        {
            menor = array[r];
        }
    }
    int numero = 2;
    cout<<"\nNumeros divisibles entre "<<numero<<":";
    for(int c=0;c<tamanio;c++){
        if(array[c]%numero==0){
            cout<<"\n"<<array[c]<<" ";
        }
    }
    
    int indice;
    cout<<"\nIngrese el indice que le va a cambiar el valor: ";
    cin>>indice;
    while(indice>tamanio || indice<0){
        cout<<"\nError.\nEl indice no existe en la lista.";
        for(int y=0;y<tamanio;y++){
            cout << "\nindice " << (y) << " Valor: " << array[y];
        }
        cout<<"\nIngrese el indice nuevamente: ";
        cin>>indice;
    }
    int valor;
    cout<<"\nIngrese el valor que desea establecer: ";
    cin>>valor;
    while(valor<0){
        cout<<"\nEl valor es incorrecto.";
        cout<<"\nIngrese el valor nuevamente: ";
        cin>>valor;
    }
    for(int a=0;a<tamanio;a++){
        array[indice]=valor;
        cout << "\nindice " << (a) << " Valor: " << array[a];
    }
    cout<<"\nEl valor maximo de la lista es: "<<mayor;
    cout << "\nEl valor minimo de la lista es: " << menor;
    
   
    return 0;
}

