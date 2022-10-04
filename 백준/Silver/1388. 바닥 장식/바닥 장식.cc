#include <iostream>
#include <cstdbool>

using namespace std;

char map[50][50];
bool visited[50][50];
int galoCnt = 0, seloCnt = 0;
int n, m;

void bfs(int y, int x) {
	visited[y][x] = true;
	char c = map[y][x];

	if (c == '-') {
		galoCnt++;
		
		while (1) {
			if (x + 1 >= m) break;

			char mc = map[y][x + 1];

			if (mc == '|') break;
			else {
				x += 1;
				visited[y][x] = true;
			}
		}
	}
	else if (c == '|') {
		seloCnt++;
		
		while (1) {
			if (y + 1 >= n) break;

			char mc = map[y + 1][x];

			if (mc == '-') break;
			else {
				y += 1;
				visited[y][x] = true;
			}
		}
	}
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++)
			cin >> map[i][j];
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (!visited[i][j])
				bfs(i, j);
		}
	}

	cout << galoCnt + seloCnt;
	return 0;
}