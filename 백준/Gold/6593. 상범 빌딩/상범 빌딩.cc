#include <iostream>
#include <cstdbool>
#include <queue>
#include <tuple>

using namespace std;

// 높이, 행, 열, 시간(초) 정보
queue<tuple<int, int, int, int>> q;
char map[30][30][30];
bool visited[30][30][30];
int l, r, c;
int endZ, endY, endX;

int dy[6] = { -1,1,0,0,0,0 };
int dx[6] = { 0,0,-1,1,0,0 };
int dz[6] = { 0,0,0,0,-1,1 };

void init() {
	q = queue<tuple<int, int, int, int>>();
	for (int k = 0; k < 30; k++) {
		for (int i = 0; i < 30; i++) {
			for (int j = 0; j < 30; j++)
				visited[k][i][j] = false;
		}
	}
}

int bfs() {
	while (!q.empty()) {
		int z = get<0>(q.front());
		int y = get<1>(q.front());
		int x = get<2>(q.front());
		int t = get<3>(q.front());
		q.pop();

		for (int i = 0; i < 6; i++) {
			int nz = z + dz[i];
			int ny = y + dy[i];
			int nx = x + dx[i];

			if (nz < 0 || ny < 0 || nx < 0 || nz >= l || ny >= r || nx >= c) continue;
			if (map[nz][ny][nx] != '#' && !visited[nz][ny][nx]) {
				if (nz == endZ && ny == endY && nx == endX) return t + 1;
				q.push({ nz,ny,nx,t+1 });
				visited[nz][ny][nx] = true;
			}
		}
	}
	return -1;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	while (1) {
		cin >> l >> r >> c;
		if (l == 0 && r == 0 && c == 0) break;

		for (int k = 0; k < l; k++) {
			for (int i = 0; i < r; i++) {
				char s[31];
				cin >> s;
				for (int j = 0; j < c; j++) {
					map[k][i][j] = s[j];
					if (s[j] == 'S') {
						q.push({ k,i,j,0 });
						visited[k][i][j] = true;
					}
					if (s[j] == 'E') {
						endZ = k;
						endY = i;
						endX = j;
					}
				}
			}
		}
		int t = bfs();
		if (t == -1) cout << "Trapped!" << '\n';
		else cout << "Escaped in " << t << " minute(s)." << '\n';
		init();
	}
	return 0;
}