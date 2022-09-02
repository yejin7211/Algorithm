#include <stdio.h>
int dp[11];

int main() {
	int N;
	scanf("%d", &N);

	dp[1] = 0;
	dp[2] = 1;
	for (int i = 3; i <= 10; i++) {
		if (i % 2 == 0) 
			dp[i] = (i / 2) * (i / 2) + dp[i / 2] + dp[i / 2];
		else 
			dp[i] = ((i + 1) / 2) * ((i - 1) / 2) + dp[(i + 1) / 2] + dp[(i - 1) / 2];
	}

	printf("%d", dp[N]);

	return 0;
}