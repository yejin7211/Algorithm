#include <iostream>
#include <cstdbool>
#include <queue>

using namespace std;

char map[250][250];
bool visited[250][250];
queue<pair<int,int>> q;
int totalWolf = 0, totalSheep = 0;
int wolf = 0, sheep = 1;
int r, c;

int dy[4] = { -1,1,0,0 };
int dx[4] = { 0,0,-1,1 };

void bfs(int y, int x) {
	visited[y][x] = true;
	q.push({ y,x });

	while (!q.empty()) {
		y = q.front().first;
		x = q.front().second;
		q.pop();

		for (int i = 0; i < 4; i++) {
			int ny = y + dy[i];
			int nx = x + dx[i];

			if (ny < 0 || nx < 0 || ny >= r || nx >= c) continue;
			if (map[ny][nx] != '#' && !visited[ny][nx]) {
				visited[ny][nx] = true;
				q.push({ ny,nx });
				if (map[ny][nx] == 'v') wolf++;
				if (map[ny][nx] == 'o') sheep++;
			}
		}
	}
	if (sheep > wolf) wolf = 0;
	else sheep = 0;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> r >> c;
	char s[251];
	for (int i = 0; i < r; i++) {
		cin >> s;
		for (int j = 0; j < c; j++) 
			map[i][j] = s[j];
	}

	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			if (map[i][j] == 'o' && !visited[i][j]) {
				wolf = 0;
				sheep = 1;
				bfs(i, j);
				totalWolf += wolf;
				totalSheep += sheep;
			}
		}
	}

	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			if (map[i][j] == 'v' && !visited[i][j])
				totalWolf++;
		}
	}
	
	cout << totalSheep << " " << totalWolf;
	return 0;
}