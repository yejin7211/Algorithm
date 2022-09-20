#include <stdio.h>
#define MAX(a,b) ( (a)>(b)?(a):(b) )
int map[301][301];
int dp[301][301];

int main() {
	int n, m;
	scanf("%d %d", &n, &m);

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			scanf("%d", &map[i][j]);
			dp[i][j] = map[i][j];
		}
	}

	int xpos[2] = { -1,0 };
	int ypos[2] = { 0,-1 };

	int max = 0;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			for (int k = 0; k < 2; k++) {
				int x = i + xpos[k];
				int y = j + ypos[k];

				if (x <= 0 || y <= 0 || x > n || y > m)
					continue;

				dp[i][j] = MAX(dp[i][j], dp[x][y] + map[i][j]);
			}
			max = MAX(max, dp[i][j]);
		}
	}

	printf("%d", max);

	return 0;
}