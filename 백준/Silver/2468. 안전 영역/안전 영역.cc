#include <iostream>
#include <cstdbool>
#include <queue>
using namespace std;

queue<pair<int, int>> q;
int map[100][100];
bool visited[100][100];
int n;

void init() {
	for (int i = 0; i < 100; i++) {
		for (int j = 0; j < 100; j++)
			visited[i][j] = false;
	}
}

void bfs(int h) {
	int my[4] = { -1,1,0,0 };
	int mx[4] = { 0,0,-1,1 };

	while (!q.empty()) {
		int y = q.front().first;
		int x = q.front().second;
		q.pop();
		for (int i = 0; i < 4; i++) {
			int ny = my[i] + y;
			int nx = mx[i] + x;
			if (ny < 0 || nx < 0 || ny >= n || nx >= n) continue;
			if (map[ny][nx] > h && !visited[ny][nx]) {
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
 
	cin >> n;
	int floodedH = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> map[i][j];
			floodedH = floodedH > map[i][j] ?
				floodedH : map[i][j];
		}
	}

	int maxAreaCnt = 0;
	for (int h = floodedH; h >= 1; h--) {
		init();
		int areaCnt = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (map[i][j] > h && !visited[i][j]) {
					q.push({ i,j });
					visited[i][j] = true;
					bfs(h);
					areaCnt++;
				}
			}
		}

		maxAreaCnt = maxAreaCnt > areaCnt ?
			maxAreaCnt : areaCnt;
	}
	if (maxAreaCnt == 0) cout << 1;
	else cout << maxAreaCnt;
	return 0;
}