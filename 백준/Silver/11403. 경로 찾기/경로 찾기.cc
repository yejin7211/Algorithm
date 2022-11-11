#include <iostream>
#include <cstring>

using namespace std;

int n;
int map[101][101];
int visited[101];

void dfs(int v) {
	for (int w = 1; w <= n; w++) {
		if (map[v][w] == 1 && !visited[w]) {
			visited[w] = 1;
			dfs(w);
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	cin >> n;
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++)
			cin >> map[i][j];

	for (int i = 1; i <= n; i++) {
		dfs(i);
		for (int j = 1; j <= n; j++) 
			cout << visited[j] << ' ';
		cout << '\n';
		memset(visited, 0, sizeof(visited));
	}
	return 0;
}