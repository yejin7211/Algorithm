#include <iostream>

using namespace std;

int n, m;
int map[1001][1001];
int visited[1001];

void search(int u) {
	visited[u] = 1;
	for (int v = 1; v <= n; v++) {
		if (!visited[v] && map[u][v] == 1)
			search(v);
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
		if (!visited[i]) {
			search(i);
			cnt++;
		}
	}
	cout << cnt;
	return 0;
}