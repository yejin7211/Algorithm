#include <iostream>
#include <cstdbool>
#include <queue>
using namespace std;

queue<pair<int, int>> q;
int map[50][50];
bool visited[50][50];
int w, h;

void init() {
	for (int i = 0; i < 50; i++) {
		for (int j = 0; j < 50; j++)
			visited[i][j] = false;
	}
}
void bfs() {
	int dy[8] = { -1,1,0,0,-1,-1,1,1 };
	int dx[8] = { 0,0,-1,1,-1,1,-1,1 };

	while (!q.empty()) {
		int y = q.front().first;
		int x = q.front().second;
		q.pop();
		for (int i = 0; i < 8; i++) {
			int ny = y + dy[i];
			int nx = x + dx[i];
			if (nx < 0 || ny < 0 || nx >= w || ny >= h) continue;
			if (map[ny][nx] == 1 && !visited[ny][nx]) {
				q.push({ ny,nx });
				visited[ny][nx] = true;
			}
		}
	}
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	while (1) {
		init();
	
		cin >> w >> h;
		if (w == 0 && h == 0)
			break;

		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++)
				cin >> map[i][j];
		}

		int cnt = 0;
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				if (!visited[i][j] && map[i][j] == 1) {
					q.push({ i,j });
					visited[i][j] = true;
					bfs();
					cnt++;
				}
			}
		}

		cout << cnt << '\n';
	}
	return 0;
}