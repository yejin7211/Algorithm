#include <stdio.h>
typedef long long ll;
ll dp[91];

int main() {
	ll N;
	scanf("%lld", &N);
	
	dp[1] = 1;
	for (ll i = 2; i <= N; i++)
		dp[i] = dp[i - 2] + dp[i - 1];

	printf("%lld", dp[N]);

	return 0;
}