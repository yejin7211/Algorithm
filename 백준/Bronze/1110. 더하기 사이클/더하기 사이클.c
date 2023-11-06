#include <stdio.h>

int main(){
    int n;
    scanf("%d", &n);
    
    int goal = n;
    int cnt = 0;
    do{
        cnt++;
        int sum = n/10+n%10;
        n = (n%10)*10+sum%10;
    }while(n!=goal);
    
    printf("%d", cnt);
    return 0;
}