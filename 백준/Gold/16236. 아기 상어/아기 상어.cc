#include <iostream>
#include <cstring>
#include <queue>
#include <tuple>

using namespace std;

int n;
int map[20][20];
int sharkY, sharkX, sharkSize = 2;
int eatenCnt = 0;
queue<tuple<int, int, int>> q; 
int movedT, movedY, movedX;
int t = 0;

void input() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> map[i][j];
			if (map[i][j] == 9) {
				sharkY = i;
				sharkX = j;
			}
		}
	}
}

void search_eatableFish() {
	int visited[20][20];
	memset(visited, 0, sizeof(visited));
	q = queue<tuple<int, int, int>>();
	int dy[4] = { -1,1,0,0 };
	int dx[4] = { 0,0,-1,1 };

	// 이동 시간, 아기상어의 y좌표, 아기상어의 x좌표
	q.push({ 0, sharkY, sharkX });
	visited[sharkY][sharkX] = 1;
	while (!q.empty()) {
		int d = get<0>(q.front());
		int y = get<1>(q.front());
		int x = get<2>(q.front());
		q.pop();
		if (map[y][x] != 9 && map[y][x] != 0 && map[y][x] < sharkSize) {
			if (d < movedT) {
				movedT = d;
				movedY = y;
				movedX = x;
			}
			else if (d == movedT) {
				if (y < movedY) {
					movedT = d;
					movedY = y;
					movedX = x;
				}
				else if (y == movedY) {
					if (x < movedX) {
						movedT = d;
						movedY = y;
						movedX = x;
					}
				}
			}
		}
		for (int i = 0; i < 4; i++) {
			int ny = y + dy[i];
			int nx = x + dx[i];
			if (ny < 0 || nx < 0 || ny >= n || nx >= n) continue;
			if (!visited[ny][nx] && map[ny][nx] <= sharkSize) {
				q.push({ d + 1,ny,nx });
				visited[ny][nx] = 1;
			}
		}
	}
}

void sol() {
	while (1) {
		movedT = 987654321;
		search_eatableFish();
		if (movedT == 987654321)
			break;

		map[sharkY][sharkX] = 0;
		sharkY = movedY;
		sharkX = movedX;
		map[sharkY][sharkX] = 9;
		t += movedT;
		eatenCnt++;
		if (eatenCnt == sharkSize) {
			sharkSize++;
			eatenCnt = 0;
		}
	}
	cout << t;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	input();
	sol();
	return 0;
}