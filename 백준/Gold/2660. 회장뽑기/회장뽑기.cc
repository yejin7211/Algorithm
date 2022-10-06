#include <iostream>

using namespace std;

int map[51][51];
int score[51];
int n;

void Floyd() {
	for (int k = 1; k <= n; k++) {
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				if (map[i][j] > map[i][k] + map[k][j])
					map[i][j] = map[i][k] + map[k][j];
			}
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	for (int i = 1; i <= 50; i++) {
		for (int j = 1; j <= 50; j++)
			map[i][j] = (i == j) ? 0 : 1000000000;
	}

	cin >> n;
	while (1) {
		int a, b;
		cin >> a >> b;
		if (a == -1 && b == -1) break;
		map[a][b] = 1;
		map[b][a] = 1;
	}

	Floyd();

	int minScore = -1;
	for (int i = 1; i <= n; i++) {
		int max = 0;
		for (int j = 1; j <= n; j++)
			max = max > map[i][j] ? max : map[i][j];
		score[i] = max;
		if (minScore == -1) minScore = max;
		else minScore = minScore < max ? minScore : max;
	}

	int hoboo = 0;
	for (int i = 1; i <= n; i++) {
		if (score[i] == minScore)
			hoboo++;
	}

	cout << minScore << ' ' << hoboo << '\n';
	for (int i = 1; i <= n; i++) {
		if (score[i] == minScore)
			cout << i << ' ';
	}
	return 0;
}