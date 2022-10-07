#include <iostream>

using namespace std;

int memo[51][51][51];

int w(int a, int b, int c) {
	if (a <= 0 || b <= 0 || c <= 0)
		return 1;
	if (a > 20 || b > 20 || c > 20)
		return w(20, 20, 20);
	if (memo[a][b][c]) return memo[a][b][c];
	
	if (a < b && b < c) {
		memo[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c);
		return memo[a][b][c];
	}
	
	memo[a][b][c] =  w(a - 1, b, c) + w(a - 1, b - 1, c)
		+ w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1);
	return memo[a][b][c];
}

int main() {
	while (1) {
		int a, b, c;
		cin >> a >> b >> c;
		if (a == -1 && b == -1 && c == -1) break;

		int ans = w(a, b, c);
		cout << "w(" << a << ", " << b << ", " << c << ") = " << ans << '\n';
	}
	return 0;
}