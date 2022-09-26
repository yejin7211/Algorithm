#include <iostream>
using namespace std;
long long dp[51];

int main() {
	long long n;
	cin >> n;
	
	dp[0] = 1;
	dp[1] = 1;
	for (int i = 2; i <= 50; i++)
		dp[i] = (dp[i - 1] + dp[i - 2] + 1) % 1000000007;

	cout << dp[n];
	return 0;
}