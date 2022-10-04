#include <iostream>
#include <cstdbool>
#include <queue>
using namespace std;

queue<pair<int, int>> q;
int map[300][300];
int l, eIdxY, eIdxX;

int my[8] = { -1,-2,-2,-1,1,2,2,1 };
int mx[8] = { -2,-1,1,2,-2,-1,1,2 };

void init() {
	q = queue<pair<int, int>>();
	for (int i = 0; i < 300; i++) {
		for (int j = 0; j < 300; j++)
			map[i][j] = 0;
	}
}

int bfs(int sIdxY, int sIdxX, int moveCnt) {
	q.push({ sIdxY, sIdxX });

	while (!q.empty()) {
		int y = q.front().first;
		int x = q.front().second;
		q.pop();

		if (y == eIdxY && x == eIdxX)
			return map[y][x];
		for (int i = 0; i < 8; i++) {
			int ny = y + my[i];
			int nx = x + mx[i];

			if (ny < 0 || nx < 0 || ny >= l || nx >= l) continue;
			if (map[ny][nx] == 0) {
				q.push({ ny,nx });
				map[ny][nx] = map[y][x] + 1;
			}
		}
	}
	return -1;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int t;
	cin >> t;
	while (t--) {
		init();
		cin >> l;
		
		int sIdxY, sIdxX;
		cin >> sIdxY >> sIdxX;
		cin >> eIdxY >> eIdxX;

		cout << bfs(sIdxY, sIdxX, 0) << '\n';
	}
	return 0;
}