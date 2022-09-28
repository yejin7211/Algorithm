#include <iostream>
#define MIN(a,b) ( (a)<(b)?(a):(b) )
#define MAX_ENERGE	9999
using namespace std;
struct Energe {
	int smallJ;
	int bigJ;
};
Energe arrE[21];
int dp[21][2];

int main() {
	int n, k;
	cin >> n;

	for (int i = 1; i < n; i++) {
		cin >> arrE[i].smallJ >> arrE[i].bigJ;
		dp[i][0] = MAX_ENERGE;
		dp[i][1] = MAX_ENERGE;
	}
	cin >> k;

	dp[n - 1][0] = arrE[n - 1].smallJ;
	if (n - 2 >= 0)
		dp[n - 2][0] = MIN(arrE[n - 2].bigJ,
			arrE[n - 2].smallJ + arrE[n - 1].smallJ);
	if (n - 3 >= 0) {
		dp[n - 3][0] = MIN(arrE[n - 3].bigJ + arrE[n - 1].smallJ,
			arrE[n - 3].smallJ + dp[n - 2][0]);
		dp[n - 3][1] = k;
	}

	for (int i = n - 4; i >= 1; i--) {
		dp[i][0] = MIN(arrE[i].smallJ + dp[i + 1][0],
			arrE[i].bigJ + dp[i + 2][0]);
		dp[i][1] = MIN(k+dp[i+3][0],
			MIN(arrE[i].smallJ + dp[i + 1][1], arrE[i].bigJ + dp[i + 2][1]));
	}
	cout << MIN(dp[1][0], dp[1][1]);
	return 0;
}