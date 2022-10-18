#include <iostream>
#define MAX(a, b) ( (a)>(b)?(a):(b) )

using namespace std;

int map[2][100000];
int dp[2][100000]; //0: 총 value, 1: 상하 정보

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int t;
	cin >> t;
	while (t--) {
		int n;
		cin >> n;
		for (int j = 0; j < n; j++)
			cin >> map[0][j];
		for (int j = 0; j < n; j++)
			cin >> map[1][j];

		dp[0][0] = map[0][0];
		dp[1][0] = map[1][0];
		dp[0][1] = map[1][0] + map[0][1];
		dp[1][1] = map[0][0] + map[1][1];
		for (int i = 2; i < n; i++) {
			dp[0][i] = map[0][i] + MAX(MAX(dp[1][i - 1], dp[0][i - 2]), dp[1][i - 2]);
			dp[1][i] = map[1][i] + MAX(MAX(dp[0][i - 1], dp[1][i - 2]), dp[0][i - 2]);
		}
		cout << MAX(dp[0][n - 1], dp[1][n - 1]) << '\n';
	}
	return 0;
}