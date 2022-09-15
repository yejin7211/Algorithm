#include <stdio.h>
#include <math.h>
#define MIN(a,b) ( (a)<(b)?(a):(b) )
int dp[100001];

int main() {
	int n;
	scanf("%d", &n);
	
	dp[1] = 1;
	dp[2] = 2;
	for (int i = 3; i <= n; i++) {
		dp[i] = dp[i - 1] + 1;
		int x = 2;
		while (int(pow(x, 2)) <= i) {
			dp[i] = MIN(dp[i], dp[i - int(pow(x, 2))] + 1);
			x++;
		}
	}

	printf("%d", dp[n]);

	return 0;
}