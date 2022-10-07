#include <iostream>
#include <cstdbool>
#include <tuple>
#include <queue>

using namespace std;

int map[101][101];
int visited[101][101];
queue<tuple<int, int, int>> q;
int n, m, t;

int dy[4] = { -1,1,0,0 };
int dx[4] = { 0,0,-1,1 };

int bfs(int y, int x, int l) {
	q.push({ y,x,l });
	visited[y][x] = 1;

	while (!q.empty()) {
		y = get<0>(q.front());
		x = get<1>(q.front());
		l = get<2>(q.front());
		q.pop();

		if (l > t) return -1;
		
		for (int i = 0; i < 4; i++) {
			int ny = y + dy[i];
			int nx = x + dx[i];

			if (ny <= 0 || nx <= 0 || ny > n || nx > m) continue;
			if (visited[y][x] == 2 && visited[ny][nx] != 2) {
				if (ny == n && nx == m)
					return l + 1;
				q.push({ ny,nx,l + 1 });
				visited[ny][nx] = 2;
			}
			else if (visited[y][x] != 2 && map[ny][nx] != 1 && visited[ny][nx] != 1) {
				if (ny == n && nx == m)
					return l + 1;
				if (map[ny][nx] == 2) {
					q.push({ ny,nx,l + 1 });
					visited[ny][nx] = 2;
				}
				else {
					q.push({ ny,nx,l + 1 });
					if (visited[ny][nx] == 0) visited[ny][nx] = 1;
				}
			}
		}
	}
	return -1;
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n >> m >> t;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++)
			cin >> map[i][j];
	}

	int t = bfs(1, 1, 0);
	if (t == -1) cout << "Fail";
	else cout << t;
	return 0;
}