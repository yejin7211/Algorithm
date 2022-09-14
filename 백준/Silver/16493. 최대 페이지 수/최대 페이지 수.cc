#include <stdio.h>
#define MAX(a,b) ( (a)>(b)?(a):(b) )
typedef struct {
	int d;
	int p;
}Book;
Book book[201];
int dp[21][201];

int main() {
	int n, m;
	scanf("%d %d", &n, &m);
	for (int i = 1; i <= m; i++) 
		scanf("%d %d", &book[i].d, &book[i].p);

	int ans = 0;
	for (int i = 1; i <= m; i++) {
		for (int j = n; j >= 0; j--) {
			if (j - book[i].d >= 0)
				dp[i][j] = MAX(dp[i - 1][j], dp[i - 1][j - book[i].d] + book[i].p);
			else dp[i][j] = dp[i - 1][j];
			ans = MAX(dp[i][j], ans);
		}
	}

	printf("%d", ans);

	return 0;
}