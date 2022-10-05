#include <iostream>
#include <cstdbool>
#include <queue>

using namespace std;

int map[1000][1000];
bool visited[1000][1000];
queue<pair<int,int>> q;
int n, m;

int dy[4] = { -1,1,0,0 };
int dx[4] = { 0,0,-1,1 };

void resetVisited() {
	for (int i = 0; i < 1000; i++) {
		for (int j = 0; j < 1000; j++)
			visited[i][j] = false;
	}
}

bool bfs(int y, int x) {
	visited[y][x] = true;
	q.push({ y,x });

	while (!q.empty()) {
		y = q.front().first;
		x = q.front().second;
		q.pop();

		for (int i = 0; i < 4; i++) {
			int ny = y + dy[i];
			int nx = x + dx[i];

			if (ny < 0 || nx < 0 || ny >= n || nx >= m) continue;
			if (map[ny][nx] == 0 && !visited[ny][nx]) {
				if (ny == n - 1) return true;
				visited[ny][nx] = true;
				q.push({ ny,nx });
			}
		}
	}
	return false;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n >> m;
	char s[1001];
	for (int i = 0; i < n; i++) {
		cin >> s;
		for (int j = 0; j < m; j++)
			map[i][j] = s[j] - '0';
	}

	for (int j = 0; j < m; j++) {
		if (map[0][j] == 0) {
			if (bfs(0, j)) {
				cout << "YES";
				return 0;
			}
		}
	}
	cout << "NO";
	return 0;
}