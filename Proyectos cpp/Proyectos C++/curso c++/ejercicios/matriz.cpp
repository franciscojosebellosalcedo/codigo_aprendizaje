#include<iostream>
using namespace std;
int main(){
    
    int matriz[3][3]={{0,0,0},{0,0,0},{0,0,0}};
    for(int i=0;i<3;i++){
        for(int x=0;x<3;x++){  
            cout<<matriz[i][x]<<" ";
            if(i!=1){
               matriz[i][x]=1;
            }
        }cout<<"\n";
    }
    return 0;
}