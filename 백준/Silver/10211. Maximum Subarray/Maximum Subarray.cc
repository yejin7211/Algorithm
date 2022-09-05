#include <stdio.h>
#include <stdlib.h>
#define MAX(a,b) ( (a)>(b)?(a):(b) )
int dp[1001];

void init() {
	for (int i = 0; i <= 1000; i++)
		dp[i] = 0;
}
int compare(const void* a, const void* b) {
	return *(int*)a - *(int*)b;
}
int main() {
	int T;
	scanf("%d", &T);

	int N, n;
	while (T--) {
		scanf("%d", &N);
		init();
		int idx = 0;

		if (N == 1) {
			scanf("%d", &n);
			printf("%d\n", n);
		}
		else {
			for (int i = 0; i < N; i++) {
				scanf("%d", &n);
				int max = MAX(dp[idx] + n, n);

				if (i == 0) dp[idx] = max;
				else if (max < dp[idx]) dp[++idx] = max;
				else dp[idx] = max;
			}

			qsort(dp, idx + 1, sizeof(int), compare);

			if (idx == 0) printf("%d\n", dp[0]);
			else printf("%d\n", dp[idx]);
		}
	}

	return 0;
}