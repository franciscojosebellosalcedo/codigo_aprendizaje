#include<iostream>
#include<math.h>
using namespace std;

void function(double x,double y){
    double expresion;
    expresion=(sqrt(x))/(pow(y,2)-1);
    cout<<expresion;
}
int main(){
    double x;
    double y;
    cout<<"Ingrese valor para x:"<<endl;
    cin>>x;
    cout<<"Ingrese valor para y:"<<endl;
    cin>>y;

    function(x,y);
    
    

    return 0;
}