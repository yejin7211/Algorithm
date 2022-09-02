#include <stdio.h>
int dp[1001];

int main() {
	int N;
	scanf("%d", &N);
	
	dp[0] = 1, dp[1] = 0, dp[2] = 1;
	for (int i = 3; i <= N; i++) {
		if (dp[i - 1] == 0) dp[i] = 1;
		else dp[i] = 0;
	}

	if (dp[N] == 1) printf("SK");
	else printf("CY");

	return 0;
}