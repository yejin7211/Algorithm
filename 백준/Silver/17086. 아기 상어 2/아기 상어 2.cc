#include <iostream>
#include <cstdbool>
#include <queue>

using namespace std;

int map[50][50];
queue<pair<int, int>> q;
int n, m, maxD = 0;

int my[8] = { -1,-1,-1,0,0,1,1,1 };
int mx[8] = { -1,0,1,-1,1,-1,0,1 };

void bfs() {
	while (!q.empty()) {
		int y = q.front().first;
		int x = q.front().second;
		q.pop();
		
		for (int i = 0; i < 8; i++) {
			int ny = y + my[i];
			int nx = x + mx[i];

			if (ny < 0 || nx < 0 || ny >= n || nx >= m) continue;
			if (!map[ny][nx]) {
				map[ny][nx] = map[y][x] + 1;
				maxD = maxD > map[ny][nx] ? maxD : map[ny][nx];
				q.push({ ny,nx });
			}
		}
	}
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> map[i][j];
			if (map[i][j] == 1) 
				q.push({ i,j });
		}
	}

	bfs();
	cout << maxD - 1;
	return 0;
}