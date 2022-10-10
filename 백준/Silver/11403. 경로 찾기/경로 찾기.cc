#include <iostream>
#include <vector>

using namespace std;

int map[101][101];
int n;

void Floyd() {
	for (int k = 1; k <= n; k++) {
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				if (map[i][k] == 1 && map[k][j] == 1)
					map[i][j] = 1;
			}
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) 
			cin >> map[i][j];
	}

	Floyd();

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++)
			cout << map[i][j] << ' ';
		cout << '\n';
	}
	return 0;
}