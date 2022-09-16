#include <iostream>
struct Arr {
	int T;
	int P;
};

int main() {
	int N;
	std::cin >> N;

	Arr arr[16];
	for (int i = 1; i <= N; i++) {
		std::cin >> arr[i].T;
		std::cin >> arr[i].P;
	}

	int dp[16];
	int max_dp = 0;
	for (int i = N; i >= 1; i--) {
		int t = arr[i].T;
		if (i + t - 1 <= N) {
			dp[i] = arr[i].P;
			int max_value = 0;
			for (int j = i + t; j <= N; j++) {
				max_value = max_value > dp[j] ? max_value : dp[j];
			}
			dp[i] += max_value;
		}
		else {
			dp[i] = 0;
		}

		max_dp = max_dp > dp[i] ? max_dp : dp[i];
	}

	std::cout << max_dp << std::endl;

	return 0;
}