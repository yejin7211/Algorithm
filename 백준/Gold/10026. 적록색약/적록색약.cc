#include <iostream>
#include <cstdbool>
#include <queue>

using namespace std;

char map[100][100];
bool visited[100][100];
queue<pair<int, int>> q;
int n;

int dy[4] = { -1,1,0,0 };
int dx[4] = { 0,0,-1,1 };

void bfs1(int y, int x) {
	while (!q.empty()) {
		y = q.front().first;
		x = q.front().second;
		visited[y][x] = true;
		q.pop();

		for (int i = 0; i < 4; i++) {
			int ny = y + dy[i];
			int nx = x + dx[i];

			if (ny < 0 || nx < 0 || ny >= n || nx >= n) continue;
			if (map[ny][nx] == map[y][x] && !visited[ny][nx]) {
				q.push({ ny,nx });
				visited[ny][nx] = true;
			}
		}
	}
}

void resetVisited() {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++)
			visited[i][j] = false;
	}
}

void bfs2(int y, int x) {
	while (!q.empty()) {
		y = q.front().first;
		x = q.front().second;
		visited[y][x] = true;
		q.pop();

		for (int i = 0; i < 4; i++) {
			int ny = y + dy[i];
			int nx = x + dx[i];

			if (ny < 0 || nx < 0 || ny >= n || nx >= n) continue;
			if (!visited[ny][nx]) {
				if ((map[y][x] == 'B' && map[ny][nx] == 'B') ||
					(map[y][x] != 'B' && map[ny][nx] != 'B')) {
					q.push({ ny,nx });
					visited[ny][nx] = true;
				}
			}
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	// 입력
	cin >> n;
	for (int i = 0; i < n; i++) {
		char s[101];
		cin >> s;
		for (int j = 0; j < n; j++)
			map[i][j] = s[j];
	}

	// 적록색약이 아닌 사람이 봤을 때
	int cnt1 = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (!visited[i][j]) {
				q.push({ i,j });
				bfs1(i, j);
				cnt1++;
			}
		}
	}

	resetVisited();

	// 적록색약인 사람이 봤을 때
	int cnt2 = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (!visited[i][j]) {
				q.push({ i,j });
				bfs2(i, j);
				cnt2++;
			}
		}
	}

	cout << cnt1 << ' ' << cnt2;
	return 0;
}