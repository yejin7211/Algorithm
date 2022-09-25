#include <stdio.h>
int main(){
    int test; scanf("%d",&test);
    int n;
    int f0[41]={1,0};
    int f1[41]={0,1};
    for(int i=2;i<=40;i++){
        f0[i]=f0[i-2]+f0[i-1];
        f1[i]=f1[i-2]+f1[i-1];
    }
    for(int i=0;i<test;i++){
        scanf("%d",&n);    
        printf("%d %d\n",f0[n],f1[n]);
    }
    return 0;
}