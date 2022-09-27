#include <iostream>
#define MOD	1000000007;
using namespace std;
long long dp[1001][1001];

int main() {
	int n, m;
	cin >> n >> m;

	dp[1][1] = 1;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			if (i == 1 && j == 1) continue;
			dp[i][j] = (dp[i][j - 1] + dp[i - 1][j] + dp[i - 1][j - 1]) % MOD;
		}
	}

	cout << dp[n][m];
	return 0;
}