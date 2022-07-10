#include<iostream>
using namespace std;
int main(){
    int n;
    cout<<"Ingrese un numero: "<<endl;
    cin>>n;
    while((n<=0)){
        cout<<"Numero no correcto."<<endl;
        cout<<"Ingrese un numero: "<<endl;
        cin>>n;
    }
    if((n>0)){
        
        int factorial;
        factorial=1;
        
        for (int i=n;i>=1;i--)
        {
            factorial=factorial*i;
            
        }
        cout<<"Factorial del numero "<<n<<" es :"<<factorial;
        
    }
    


    return 0;
}