#include<iostream>
using namespace std;
int main(){
    int array[]={1,2,3,4,5,6};
    int acum=0;
    for(int i=0;i<6;i++){
        acum=acum+array[i];
    }
    cout<<"Suma total: "<<acum<<endl;

    return 0;
}