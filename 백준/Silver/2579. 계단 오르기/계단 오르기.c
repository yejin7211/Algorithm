#include <stdio.h>
#define MAX(a,b) a>b?a:b
int main() {
	int N;
	int stair[301] = { 0, };
	int dp[301] = { 0, };
	scanf("%d", &N);
	for (int i = 1; i <= N; i++)
		scanf("%d", &stair[i]);

	dp[0] = 0;
	dp[1] = stair[1];
	dp[2] = stair[1] + stair[2];
	for (int i = 3; i <= N; i++) {
		dp[i] = MAX(stair[i] + dp[i - 2], stair[i] + stair[i - 1] + dp[i - 3]);
	}

	printf("%d\n", dp[N]);
	return 0;
}