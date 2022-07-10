#include<iostream>
using namespace std;
int main(){
    double notaPractica,notaTeorica,notaParticipacion;
    cout<<"Ingrese la nota practica: ";
    cin>>notaPractica;
    cout<<"Ingrese la nota teorica: ";
    cin>>notaTeorica;
    cout<<"Ingrese la nota de participacion: ";
    cin>>notaParticipacion;
    notaPractica=notaPractica*0.30;
    notaTeorica=notaTeorica*0.60;
    notaParticipacion = notaParticipacion*0.10;
    double notaFinal;
    notaFinal=notaPractica+notaTeorica+notaParticipacion;
    cout.precision(2);
    cout << "\nLa nota final del estudiante es de: " << notaFinal;
    return 0;
}