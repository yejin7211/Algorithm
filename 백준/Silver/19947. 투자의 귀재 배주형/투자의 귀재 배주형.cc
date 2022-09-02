#include <stdio.h>
#define MAX(a,b) ( (a)>(b)?(a):(b) )
typedef long long ll;
ll dp[11];

int main() {
	int H, Y;
	scanf("%d %d", &H, &Y);

	dp[0] = H;
	dp[1] = H * 1.05;
	dp[2] = dp[1] * 1.05;
	dp[3] = MAX(dp[2] * 1.05, dp[0] * 1.2);
	dp[4] = MAX(dp[3] * 1.05, dp[1] * 1.2);

	for (int i = 5; i <= 10; i++) {
		dp[i] = MAX(dp[i - 1] * 1.05, dp[i - 3] * 1.2);
		dp[i] = MAX(dp[i], dp[i - 5] * 1.35);
	}

	printf("%lld", dp[Y]);
	
	return 0;
}