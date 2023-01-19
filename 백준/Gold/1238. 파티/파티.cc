#include <iostream>
#define MIN(a, b) ( (a)<(b)?(a):(b) )
#define MAX(a, b) ( (a)>(b)?(a):(b) )

using namespace std;

int graph[1001][1001];

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n, m, x;
	cin >> n >> m >> x;
	
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			graph[i][j] = 987654321;
			if (i == j) graph[i][j] = 0;
		}
	}
	while (m--) {
		int s, e, t;
		cin >> s >> e >> t;
		graph[s][e] = t;
	}

	for (int k = 1; k <= n; k++) {
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++)
				graph[i][j] = MIN(graph[i][j], graph[i][k] + graph[k][j]);
		}
	}

	int answer = -1;
	for (int i = 1; i <= n; i++) {
		answer = MAX(answer, graph[i][x] + graph[x][i]);
	}
	cout << answer;
	return 0;
}