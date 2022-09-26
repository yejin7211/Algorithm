#include <iostream>
using namespace std;
long long dp[1000001];

int main() {
	long long t, n;
	cin >> t;

	dp[1] = 1;
	dp[2] = 2;
	dp[3] = 4;
	for (long long i = 4; i <= 1000000; i++) {
		dp[i] = (dp[i - 3] + dp[i - 2] + dp[i - 1]) % 1000000009;
	}

	while (t--) {
		cin >> n;
		cout << dp[n] << endl;
	}
	return 0;
}