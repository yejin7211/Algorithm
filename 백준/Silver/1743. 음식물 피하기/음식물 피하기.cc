#include <iostream>
#include <cstdbool>
#include <queue>

using namespace std;

int food[101][101];
queue<pair<int, int>> q;
int n, m, k;
int foodSize = 0;
int maxSize = 0;

int dy[4] = { -1,1,0,0 };
int dx[4] = { 0,0,-1,1 };

void bfs(int y, int x) {
	food[y][x] = 0;
	q.push({ y,x });
	foodSize++;

	while (!q.empty()) {
		int y = q.front().first;
		int x = q.front().second;
		q.pop();

		for (int i = 0; i < 4; i++) {
			int ny = y + dy[i];
			int nx = x + dx[i];

			if (ny < 0 || nx < 0 || ny > n || nx > m) continue;
			if (food[ny][nx] == 1) {
				food[ny][nx] = 0;
				q.push({ ny,nx });
				foodSize++;
			}
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n >> m >> k;
	while (k--) {
		int r, c;
		cin >> r >> c;
		food[r][c] = 1;
	}

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			if (food[i][j] == 1) {
				bfs(i, j);
				maxSize = maxSize > foodSize ?
					maxSize : foodSize;
				foodSize = 0;
			}
		}
	}
	cout << maxSize;
	return 0;
}