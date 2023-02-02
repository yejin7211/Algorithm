#include <iostream>

using namespace std;

int heights[500][500];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n, m, b;
	cin >> n >> m >> b;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++)
			cin >> heights[i][j];
	}

	int minTime = -1;
	int maxHeight = -1;
	for (int h = 0; h <= 256; h++) {
		int Time = 0;
		int blocks = b;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (heights[i][j] > h) {
					Time += 2 * (heights[i][j] - h);
					blocks += heights[i][j] - h;
				}
				else if (heights[i][j] < h) {
					Time += h - heights[i][j];
					blocks -= h - heights[i][j];
				}
			}
		}

		if (blocks >= 0) {
			if (minTime == -1 || Time <= minTime) {
				minTime = Time;
				maxHeight = h;
			}
		}
	}

	cout << minTime << ' ' << maxHeight;

	return 0;
}