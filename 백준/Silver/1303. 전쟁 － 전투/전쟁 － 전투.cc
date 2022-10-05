#include <iostream>
#include <cstdbool>
#include <queue>

using namespace std;

char map[100][100];
bool visited[100][100];
queue<pair<int, int>> q;
int myPower = 0, yourPower = 0;
int cnt = 0;
int n, m;

int dy[4] = { -1,1,0,0 };
int dx[4] = { 0,0,-1,1 };

void dfs(int y, int x, char status) {
	visited[y][x] = true;
	q.push({ y,x });
	cnt++;

	while (!q.empty()) {
		y = q.front().first;
		x = q.front().second;
		q.pop();

		for (int i = 0; i < 4; i++) {
			int ny = y + dy[i];
			int nx = x + dx[i];

			if (ny < 0 || nx < 0 || ny >= m || nx >= n) continue;
			if (map[ny][nx]==status && !visited[ny][nx]) {
				visited[ny][nx] = true;
				q.push({ ny,nx });
				cnt++;
			}
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n >> m;
	for (int i = 0; i < m; i++) {
		char s[101];
		cin >> s;
		for (int j = 0; j < n; j++) 
			map[i][j] = s[j];
	}

	// 우리팀 병사 위력 확인
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			if (map[i][j] == 'W' && !visited[i][j]) {
				dfs(i, j, 'W');
				myPower += cnt * cnt;
				cnt = 0;
			}
		}
	}

	// 상대팀 병사 위력 확인
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			if (map[i][j] == 'B' && !visited[i][j]) {
				dfs(i, j, 'B');
				yourPower += cnt * cnt;
				cnt = 0;
			}
		}
	}

	cout << myPower << " " << yourPower;
	return 0;
}