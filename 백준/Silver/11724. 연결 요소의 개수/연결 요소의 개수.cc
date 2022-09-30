#include <iostream>
#include <cstdbool>
using namespace std;
int map[1001][1001];
bool visited[1001][1001];
int n, m;

void bfs(int rowIdx) {
	for (int i = 1; i <= n; i++)
		visited[i][rowIdx] = true;

	for (int j = 1; j <= n; j++) {
		if (map[rowIdx][j] == 1) {
			if (!visited[rowIdx][j]) bfs(j);

		}
	}
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n >> m;

	while (m--) {
		int u, v;
		cin >> u >> v;
		map[u][v] = 1;
		map[v][u] = 1;
	}

	int cnt = 0;
	for (int i = 1; i <= n; i++) {
		if (!visited[1][i]) {
			bfs(i);
			cnt++;
		}
	}

	cout << cnt;
	return 0;
}