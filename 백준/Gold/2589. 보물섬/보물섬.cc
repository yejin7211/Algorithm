#include <iostream>
#include <cstdbool>
#include <tuple>
#include <queue>

using namespace std;

char map[50][50];
bool visited[50][50];
queue<tuple<int, int, int>> q;
int maxT = -1;
int l, w;

int dy[4] = { -1,1,0,0 };
int dx[4] = { 0,0,-1,1 };

void reset() {
	for (int i = 0; i < 50; i++) {
		for (int j = 0; j < 50; j++)
			visited[i][j] = false;
	}
}

int bfs(int y, int x, int t) {
	q.push({ y,x,t });
	visited[y][x] = true;

	while (!q.empty()) {
		y = get<0>(q.front());
		x = get<1>(q.front());
		t = get<2>(q.front());
		q.pop();

		for (int i = 0; i < 4; i++) {
			int ny = y + dy[i];
			int nx = x + dx[i];

			if (ny < 0 || nx < 0 || ny >= l || nx >= w) continue;
			if (map[ny][nx] == 'L' && !visited[ny][nx]) {
				q.push({ ny,nx,t + 1 });
				visited[ny][nx] = true;
			}
		}
	}
	return t;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> l >> w;
	for (int i = 0; i < l; i++) {
		char s[51];
		cin >> s;
		for (int j = 0; j < w; j++)
			map[i][j] = s[j];
	}

	for (int i = 0; i < l; i++) {
		for (int j = 0; j < w; j++) {
			if (map[i][j] == 'L') {
				int t = bfs(i, j, 0);
				maxT = maxT > t ? maxT : t;
				reset();
			}
		}
	}

	cout << maxT;
	return 0;
}
