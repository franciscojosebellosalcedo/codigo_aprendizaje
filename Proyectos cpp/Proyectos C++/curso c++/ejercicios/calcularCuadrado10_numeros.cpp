#include<iostream>
#include<math.h>
using namespace std;
int main(){
    int i;
    int suma;
    suma=0;
    for(i=1;i<=10;i++){
        int cuadrado;
        cuadrado=(int)(pow(i,2));
        suma=suma+cuadrado;
    }
    cout<<"La suma del cuadrado de los 10 primeros numero es: "<<suma;

    return 0;
}