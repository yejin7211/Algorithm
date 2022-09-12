#include <stdio.h>
#define MIN(a,b) ( (a)<(b)?(a):(b) )
int dp[100000];

int main() {
	int n;
	scanf("%d", &n);

	dp[0] = 0;
	dp[1] = dp[2] = dp[5] = dp[7] = 1;
	dp[3] = dp[4] = dp[6] = 2;

	for (int i = 8; i <= n; i++) {
		if (i % 7 == 0) dp[i] = i / 7;
		else {
			dp[i] = MIN(dp[i - 5], MIN(dp[i - 2], dp[i - 1])) + 1;
		}
	}

	printf("%d", dp[n]);

	return 0;
}