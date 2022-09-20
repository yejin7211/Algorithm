#include <stdio.h>
#define MAX(a,b) ( (a)>(b)?(a):(b) )
int map[1001][1001];
int dp[1001][1001];

int main() {
	int n, m;
	scanf("%d %d", &n, &m);

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++)
			scanf("%d", &map[i][j]);
	}

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++)
			dp[i][j] = map[i][j] + MAX(dp[i - 1][j], MAX(dp[i][j - 1], dp[i - 1][j - 1]));
	}

	printf("%d", dp[n][m]);

	return 0;
}