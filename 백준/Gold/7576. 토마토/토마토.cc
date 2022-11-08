#include <iostream>
#include <queue>

using namespace std;

int m, n;
int map[1000][1000];
queue<pair<int, int>> q;
int unripen = 0;

void input() {
	cin >> m >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> map[i][j];
			if (map[i][j] == 1) q.push({ i,j });
			else if (map[i][j] == 0) unripen++;
		}
	}
}

void sol() {
	int dy[4] = { -1,1,0,0 };
	int dx[4] = { 0,0,-1,1 };

	int day = 0;
	while (!q.empty()) {
		int move = q.size();
		while (move--) {
			int y = q.front().first;
			int x = q.front().second;
			q.pop();
			for (int i = 0; i < 4; i++) {
				int ny = y + dy[i];
				int nx = x + dx[i];
				if (ny < 0 || nx < 0 || ny >= n || nx >= m) continue;
				if (map[ny][nx] == 0) {
					q.push({ ny,nx });
					map[ny][nx] = 1;
					unripen--;
				}
			}
		}
		day++;
	}
	if (unripen == 0) cout << day - 1;
	else cout << -1;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	input();
	sol();
	return 0;
}