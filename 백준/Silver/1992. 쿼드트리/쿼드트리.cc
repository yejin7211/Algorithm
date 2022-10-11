#include <iostream>

using namespace std;

int map[65][65];
int n;

int check(int n, int y, int x) {
	int num = map[y][x];
	for (int i = y; i < y + n; i++) 
		for (int j = x; j < x + n; j++)
			if (map[i][j] != num) return 0;
	return 1;
}

void solve(int n, int y, int x) {
	if (check(n, y, x)) {  // 영상 숫자가 모두 같음
		cout << map[y][x];
		return;
	}
	
	cout << "(";
	solve(n / 2, y, x);
	solve(n / 2, y, x + n / 2);
	solve(n / 2, y + n / 2, x);
	solve(n / 2, y + n / 2, x + n / 2);
	cout << ")";
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;
	for (int i = 1; i <= n; i++) {
		char s[65];
		cin >> s;
		for (int j = 1; j <= n; j++)
			map[i][j] = s[j - 1] - '0';
	}
	
	solve(n, 1, 1);
	return 0;
}