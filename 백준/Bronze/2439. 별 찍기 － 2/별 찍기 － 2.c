#include <stdio.h>

int main(){
    int n;
    scanf("%d", &n);
    
    for(int r=1;r<=n;r++){
        int cnt = n-r;
        for(int c=0;c<cnt;c++)
            printf(" ");
        for(int c=0;c<r;c++)
            printf("*");
        printf("\n");
    }
    return 0;
}