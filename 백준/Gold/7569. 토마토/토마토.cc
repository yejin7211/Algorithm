#include <iostream>
#include <tuple>
#include <queue>

using namespace std;

int m, n, h;
int map[100][100][100];
queue<tuple<int, int, int>> q;
int unripen = 0;

void input() {
	cin >> m >> n >> h;
	for (int z = 0; z < h; z++) {
		for (int y = 0; y < n; y++) {
			for (int x = 0; x < m; x++) {
				cin >> map[z][y][x];
				if (map[z][y][x] == 1) q.push({ z,y,x });
				else if (map[z][y][x] == 0) unripen++;
			}
		}
	}
}

void bfs() {
	int dz[6] = { 0,0,0,0,-1,1 };
	int dy[6] = { -1,1,0,0,0,0 };
	int dx[6] = { 0,0,-1,1,0,0 };
	
	int day = 0;
	while (!q.empty()) {
		int move = q.size();
		while (move--) {
			int z = get<0>(q.front());
			int y = get<1>(q.front());
			int x = get<2>(q.front());
			q.pop();

			for (int i = 0; i < 6; i++) { // 상하좌우
				int nz = z + dz[i];
				int ny = y + dy[i];
				int nx = x + dx[i];
				if (ny < 0 || nx < 0 || nz < 0 || ny >= n || nx >= m || nz >= h) continue;
				if (map[nz][ny][nx] == 0) {
					q.push({ nz,ny,nx });
					map[nz][ny][nx] = 1;
					unripen--;
				}
			}
		}
		day++;
	}
	if (unripen == 0)
		cout << day - 1;
	else
		cout << -1;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	input();
	bfs();
	return 0;
}