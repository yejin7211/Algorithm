#include <iostream>
#include <cstdlib>
using namespace std;

int map[101][101];
int n, a, b;
int prev1 = a;
int flag = 0;

void sol(int r) {
	for (int j = 1; j <= n; j++) {
		if (map[r][j] == 1 && j != prev1) 
			map[r][j] = map[prev1][r] + 1;
	}
	int p = prev1;
	for (int j = 1; j <= n; j++) {
		if (map[r][j] != 0 && j != p) {
			if (j == b) {
				cout << map[r][j];
				flag = 1;
				return;
			}
			prev1 = r;
			sol(j);
		}
	}
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;
	cin >> a >> b;
	
	int m;
	cin >> m;
	while (m--) {
		int x, y;
		cin >> x >> y;
		map[x][y] = 1;
		map[y][x] = 1;
	}
	
	sol(a);
	if (!flag)
		cout << -1;

	return 0;
}