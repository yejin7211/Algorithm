#include <iostream>
#define MAX	100000
typedef long long ll;

using namespace std;

struct NumCount {
	ll cnt1;
	ll cnt2;
	ll cnt3;
};
NumCount cntArr[MAX + 1];
ll dp[MAX + 1];

int main() {
	ll t, n;
	cin >> t;

	cntArr[1].cnt1 = 1; cntArr[1].cnt2 = 0; cntArr[1].cnt3 = 0; dp[1] = 1;
	cntArr[2].cnt1 = 0; cntArr[2].cnt2 = 1; cntArr[2].cnt3 = 0; dp[2] = 1;
	cntArr[3].cnt1 = 1; cntArr[3].cnt2 = 1; cntArr[3].cnt3 = 1; dp[3] = 3;
	
	for (int i = 4; i <= MAX; i++) {
		cntArr[i].cnt1 = (cntArr[i - 1].cnt2 + cntArr[i - 1].cnt3) % 1000000009;
		cntArr[i].cnt2 = (cntArr[i - 2].cnt1 + cntArr[i - 2].cnt3) % 1000000009;
		cntArr[i].cnt3 = (cntArr[i - 3].cnt1 + cntArr[i - 3].cnt2) % 1000000009;
		dp[i] = (cntArr[i].cnt1 + cntArr[i].cnt2 + cntArr[i].cnt3) % 1000000009;
	}

	while (t--) {
		cin >> n;
		cout << dp[n] << endl;
	}
	return 0;
}