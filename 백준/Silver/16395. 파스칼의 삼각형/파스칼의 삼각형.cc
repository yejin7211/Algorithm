#include <stdio.h>
int dp[31][31];

int main() {
	int n, k;
	scanf("%d %d", &n, &k);

	dp[0][0] = 1;
	dp[1][0] = 1;
	dp[1][1] = 1;
	for (int i = 2; i <= n; i++) {
		for (int j = 0; j <= i; j++) {
			if (j == 0) dp[i][0] = 1;
			else if (i == j) dp[i][j] = 1;
			else dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
		}
	}

	printf("%d", dp[n - 1][k - 1]);

	return 0;
}