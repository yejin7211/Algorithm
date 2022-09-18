#include <iostream>
int a[1001];
int dp[1001];

int main() {
	int n;
	std::cin >> n;

	for (int i = 1; i <= n; i++)
		std::cin >> a[i];

	for (int i = n; i >= 1; i--) {
		if (i == n) dp[i] = 0;
		else if (a[i] == 0) dp[i] = -1;
		else {
			int min_jump = 999;
			int onoff = 0;
			for (int j = i + 1; j <= i + a[i] && j <= n; j++) {
				if (dp[j] == -1) {
					onoff = 1;
					continue;
				}
				min_jump = min_jump < dp[j] ? min_jump : dp[j];
			}
			if (min_jump == 999 && onoff) dp[i] = -1;
			else dp[i] = min_jump + 1;
		}
	}

	std::cout << dp[1];
	
	return 0;
}