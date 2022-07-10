#include<iostream>
using namespace std;
int main (){
    double notafinal1=0, notafinal2=0, notafinal3=0, notafinal4=0;
    double media;
    cout<<"Ingrese la nota final del estudiante 1: ";
    cin>>notafinal1;
    while((notafinal1<0) ||  (notafinal1>5.0))
    {
        cout<<"La nota "<<notafinal1<<" es incorrecta.";
        cout << "\nIngrese la nota final del estudiante 1 nuevamente: ";
        cin >> notafinal1;
    }
    cout<<"Ingrese la nota final del estudiante 2: ";cin>>notafinal2;
    while((notafinal2<0)||(notafinal2>5.0))
    {
        cout<<"La nota "<<notafinal2<<" es incorrecta.";
        cout << "\nIngrese la nota final del estudiante 2 nuevamente: ";
        cin >> notafinal2;
    }
    cout<<"Ingrese la nota final del estudiante 3: ";cin>>notafinal3;
    while ((notafinal3 < 0) || (notafinal3 > 5.0))
    {
        cout << "La nota " << notafinal3 << " es incorrecta.";
        cout << "\nIngrese la nota final del estudiante 3 nuevamente: ";
        cin >> notafinal3;
    }
    cout<<"Ingrese la nota final del estudiante 4: ";cin>>notafinal4;
    while ((notafinal4 < 0) || (notafinal4 > 5.0))
    {
        cout << "La nota " << notafinal4 << " es incorrecta.";
        cout << "\nIngrese la nota final del estudiante 2 nuevamente: ";
        cin >> notafinal4;
    }
    media=(notafinal1+notafinal2+notafinal3+notafinal4)/4;
    cout.precision(2);
    cout<<"La media de las notas en total es: "<<media;
    if((media>1.0)&& (media<3.0))
    {
        cout<<"\nEl resultado de la media de las notas es muy baja.";
    }else if((media==3.0)|| ((media>3.0)&& (media<4.0)))
    {
        cout<<"\nEl resultado de la media de las notas es  estandar.";
    }else if((media>=3.9) && (media<=5.0))
    {
        cout<<"\nEl resultado de la media de la notas es muy alta.";
    }
    

    return 0;
}