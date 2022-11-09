#include <stdio.h>
long long int dp[101];
int T, N;
void solution() {
	dp[0] = dp[1] = dp[2] = 1;
	dp[3] = dp[4] = 2;
	for (long long int n = 5; n < 101; n++) 
		dp[n] = dp[n - 5] + dp[n - 1];
}
int main() {
	scanf("%d", &T);
	solution();
	
	for (int i = 0; i < T; i++) {
		scanf("%d", &N);
		printf("%lld\n", dp[N - 1]);
	}
	return 0;
}