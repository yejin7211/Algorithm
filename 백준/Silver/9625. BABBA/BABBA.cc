#include <stdio.h>
typedef struct {
	int cntA;
	int cntB;
}DP;	
DP dp[46];

void init(DP* p) {
	p[0].cntA = 1;
	p[0].cntB = 0;

	p[1].cntA = 0;
	p[1].cntB = 1;	
}

int main() {
	int K;
	scanf("%d", &K);

	init(dp);

	for (int i = 2; i <= K; i++) {
		dp[i].cntA = dp[i - 2].cntA + dp[i - 1].cntA;
		dp[i].cntB = dp[i - 2].cntB + dp[i - 1].cntB;
	}

	printf("%d %d", dp[K].cntA, dp[K].cntB);

	return 0;
}