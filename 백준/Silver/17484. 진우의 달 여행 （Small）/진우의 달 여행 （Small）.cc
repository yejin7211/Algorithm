#include <stdio.h>
#include <stdbool.h>
int n, m;
int map[7][7];
int dp[7][7];
int min = 10000;

bool isPossible(int pos) {
	if (pos<1 || pos>m) return false;
	else return true;
}

void dfs(int y, int x, int way, int total) {
	if (y == n) {
		min = min < total ? min : total;
		return;
	}

	for (int w = -1; w <= 1; w++) {
		if (way != w && isPossible(x + w)) {
			dfs(y + 1, x + w, w, total + map[y + 1][x + w]);
		}
	}
}

int main() {
	scanf("%d %d", &n, &m);

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++)
			scanf("%d", &map[i][j]);
	}

	for (int j = 1; j <= m; j++) 
		dfs(1, j, -2, map[1][j]);

	printf("%d", min);

	return 0;
}