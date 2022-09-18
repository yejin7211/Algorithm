#include <stdio.h>
int dp[191230];

int main(){
    int t, n;
    scanf("%d",&t);
    
    dp[1]=1;
    dp[2]=2;
    for(int i=3;i<=191229;i++)
        dp[i]=(dp[i-1]+dp[i-2])%1000000007;
    
    while(t--){
        scanf("%d",&n);
        printf("%lld\n",dp[n]);
    }
    return 0;
}