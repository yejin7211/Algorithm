#include <iostream>
#include <queue>

using namespace std;

struct PipeInfo {
	int y;
	int x;
	int status; //1: 가로, 2: 세로, 3: 대각선 아래
};

queue<PipeInfo> q;
int map[17][17];
int n;

void input() {
	cin >> n;
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++)
			cin >> map[i][j];
}

void bfs() {
	int cnt = 0;

	q.push({ 1,2,1 });
	while (!q.empty()) {
		int y = q.front().y;
		int x = q.front().x;
		int status = q.front().status;
		q.pop();

		if (x == n && y == n) 
			cnt++;

		switch (status) {
		case 1:
			if (x + 1 <= n && map[y][x + 1] == 0) {
				q.push({ y,x + 1,1 });
				if (y + 1 <= n && map[y + 1][x + 1] == 0 &&
					map[y][x + 1] == 0 && map[y + 1][x] == 0)
					q.push({ y + 1,x + 1,3 });
			}
			break;
		case 2:
			if (y + 1 <= n && map[y + 1][x] == 0) {
				q.push({ y + 1,x,2 });
				if (x + 1 <= n && map[y + 1][x + 1] == 0 &&
					map[y + 1][x] == 0 && map[y][x + 1] == 0)
					q.push({ y + 1,x + 1,3 });
			}
			break;
		case 3:
			if (x + 1 <= n && y + 1 <= n && map[y + 1][x + 1] == 0 &&
				map[y][x + 1] == 0 && map[y + 1][x] == 0) 
				q.push({ y + 1,x + 1,3 });
			if (x + 1 <= n && map[y][x + 1] == 0) q.push({ y,x + 1,1 });
			if (y + 1 <= n && map[y + 1][x] == 0) q.push({ y + 1,x,2 });
			break;
		}
	}

	cout << cnt;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	input();
	bfs();
	return 0;
}