#include <stdio.h>
typedef long long ll;
ll dp[32][32];

int main() {
	ll R, C, W; //3 1 4
	scanf("%lld %lld %lld", &R, &C, &W);

	dp[0][0] = 1;
	ll cnt = 2;
	ll sum = 0;
	ll count = 0;
	ll onoff = 0;
	if (R == 1) {
		sum += 1;
		onoff = 1;
		count++;
	}
	for (ll i = 1; i < R + W - 1; i++) {
		if (i == R - 1) onoff = 1; //
		if (onoff == 1) count++;

		ll tmpCount = count;
		for (ll j = 0; j < cnt; j++) {
			if (j == 0) dp[i][j] = 1;
			else if (j == cnt - 1) dp[i][j] = 1;
			else dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];

			if (tmpCount > 0 && j >= C - 1) {
				sum += dp[i][j];
				tmpCount--;
			}
		}

		if (count == W)
			break;

		cnt++;
	}

	printf("%lld", sum);

	return 0;
}