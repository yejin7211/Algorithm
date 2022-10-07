#include <iostream>

using namespace std;

int dp[10];

void func(int s) {
	int sum = 0;
	for (int i = s; i < 10; i++)
		sum += dp[i] % 10007;
	if (s < 10) dp[s] = sum;
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n;
	cin >> n;
	for (int i = 0; i < 10; i++)
		dp[i] = 10 - i;

	if (n == 1) cout << 10;
	else if (n == 2) cout << 55;
	else {
		n -= 2;
		int total = 0;
		while (n--) {
			for (int i = 0; i < 10; i++)
				func(i);
		}
		for (int i = 0; i < 10; i++) {
			total += dp[i];
			total %= 10007;
		}
		cout << total;
	}

	return 0;
}