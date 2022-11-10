#include <stdio.h>
int dp[1001];
int n;

void solution() {
	dp[1] = 1;
	dp[2] = 3;
	dp[3] = 5;
	for (int i = 4; i <= n; i++) 
		dp[i] = (dp[i - 1] + dp[i - 2] * 2)%10007;
}

int main() {
	scanf("%d", &n);
	solution();
	printf("%d\n", dp[n]);
	return 0;
}

/*
if
n=1, ans=(네모0개: 1)=1
n=2, ans=(네모1개: 1)+(네모0개: 2)=3
n=3, ans=(네모1개: 2)+(네모0개: 3)=5
n=4, ans=(네모2개: 1)+(네모1개: 5)+(네모0개: 5)=11
n=5, ans=(네모2개: 3)+(네모1개: 10)+(네모0개: 8)=21
...
*/