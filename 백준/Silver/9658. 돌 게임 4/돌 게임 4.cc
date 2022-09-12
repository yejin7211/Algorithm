#include <stdio.h>

int main() {
	int n;
	scanf("%d", &n);

	int dp[1001];
	dp[1] = 2;
	dp[2] = 1;
	dp[3] = 2;
	dp[4] = 1;
	for (int i = 5; i <= n; i++) {
		if (dp[i - 1] == 2 || dp[i - 3] == 2 || dp[i - 4] == 2)
			dp[i] = 1;
		else dp[i] = 2;
	}

	if (dp[n] == 1) printf("SK");
	else printf("CY");

	return 0;
}