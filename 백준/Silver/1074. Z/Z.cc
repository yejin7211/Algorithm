#include <iostream>
#include <cmath>
using namespace std;
int map[15][15];
int n, r, c;
int ans;

void func(int y, int x, int len) {
	if (y == r && x == c) {
		cout << ans;
		return;
	}

	if (y <= r && r < y + len && x <= c && c < x + len) {
		func(y, x, len / 2); //1사분면
		func(y, x + len / 2, len / 2); //2사분면
		func(y + len / 2, x, len / 2); //3사분면
		func(y + len / 2, x + len / 2, len / 2); //4사분면
	}
	else ans += len * len;
}
int main() {
	cin >> n >> r >> c;
	func(0, 0, pow(2, n));
	return 0;
}