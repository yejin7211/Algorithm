#include <stdio.h>

int main() {
	int n;
	scanf("%d", &n);

	int dp[1001];
	dp[1] = 1;
	dp[2] = 2;
	dp[3] = 1;
	dp[4] = 1;
	for (int i = 5; i <= n; i ++) {
		if (dp[i - 4] == 1 && dp[i - 3] == 1 && dp[i - 1] == 1)
			dp[i] = 2;
		else dp[i] = 1;
	}

	if (dp[n] == 1) printf("SK");
	else printf("CY");

	return 0;
}