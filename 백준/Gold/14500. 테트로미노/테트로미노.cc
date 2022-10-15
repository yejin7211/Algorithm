#include <iostream>

using namespace std;

int map[500][500];
int n, m;
int maxSum = 0;

void input() {
	cin >> n >> m;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			cin >> map[i][j];
}

void tetro1(int y, int x) {
	if (x + 3 < m) {
		int sum = 0;
		for (int j = x; j <= x + 3; j++)
			sum += map[y][j];
		maxSum = maxSum > sum ? maxSum : sum;
	}
	if (y + 3 < n) {
		int sum = 0;
		for (int i = y; i <= y + 3; i++)
			sum += map[i][x];
		maxSum = maxSum > sum ? maxSum : sum;
	}
}
void tetro2(int y, int x) {
	int sum = 0;
	for (int i = y; i <= y + 1; i++)
		for (int j = x; j <= x + 1; j++)
			sum += map[i][j];
	maxSum = maxSum > sum ? maxSum : sum;
}
void tetro3(int y, int x) {
	if (y + 2 < n && x + 1 < m) {
		int sum = map[y][x] + map[y + 1][x] + map[y + 2][x] + map[y + 2][x + 1];
		maxSum = maxSum > sum ? maxSum : sum;
	}
	if (y + 2 < n && x - 1 >= 0) {
		int sum = map[y][x] + map[y + 1][x] + map[y + 2][x] + map[y + 2][x - 1];
		maxSum = maxSum > sum ? maxSum : sum;
	}
	if (y + 1 < n && x + 2 < m) {
		int sum = map[y][x] + map[y][x + 1] + map[y][x + 2] + map[y + 1][x];
		maxSum = maxSum > sum ? maxSum : sum;
	}
	if (y + 1 < n && x + 2 < m) {
		int sum = map[y][x] + map[y][x + 1] + map[y][x + 2] + map[y + 1][x + 2];
		maxSum = maxSum > sum ? maxSum : sum;
	}
	if (y + 2 < n && x + 1 < m) {
		int sum = map[y][x] + map[y][x + 1] + map[y + 1][x + 1] + map[y + 2][x + 1];
		maxSum = maxSum > sum ? maxSum : sum;
	}
	if (y + 2 < n && x - 1 >= 0) {
		int sum = map[y][x] + map[y][x - 1] + map[y + 1][x - 1] + map[y + 2][x - 1];
		maxSum = maxSum > sum ? maxSum : sum;
	}
	if (y - 1 >= 0 && x + 2 < m) {
		int sum = map[y][x] + map[y][x + 1] + map[y][x + 2] + map[y - 1][x + 2];
		maxSum = maxSum > sum ? maxSum : sum;
	}
	if (y + 1 < n && x + 2 < m) {
		int sum = map[y][x] + map[y + 1][x] + map[y + 1][x + 1] + map[y + 1][x + 2];
		maxSum = maxSum > sum ? maxSum : sum;
	}
}
void tetro4(int y, int x) {
	if (y + 2 < n && x + 1 < m) {
		int sum = map[y][x] + map[y + 1][x] + map[y + 1][x + 1] + map[y + 2][x + 1];
		maxSum = maxSum > sum ? maxSum : sum;
	}
	if (y - 1 >= 0 && x + 2 < m) {
		int sum = map[y][x] + map[y][x + 1] + map[y - 1][x + 1] + map[y - 1][x + 2];
		maxSum = maxSum > sum ? maxSum : sum;
	}
	if (y + 1 < n && x + 2 < m) {
		int sum = map[y][x] + map[y][x + 1] + map[y + 1][x + 1] + map[y + 1][x + 2];
		maxSum = maxSum > sum ? maxSum : sum;
	}
	if (y + 2 < n && x - 1 >= 0) {
		int sum = map[y][x] + map[y + 1][x] + map[y + 1][x - 1] + map[y + 2][x - 1];
		maxSum = maxSum > sum ? maxSum : sum;
	}
}
void tetro5(int y, int x) {
	if (y + 1 < n && x + 2 < m) {
		int sum = map[y][x] + map[y][x + 1] + map[y][x + 2] + map[y + 1][x + 1];
		maxSum = maxSum > sum ? maxSum : sum;
	}
	if (y + 1 < n && y - 1 >= 0 && x + 1 < m) {
		int sum = map[y][x] + map[y - 1][x + 1] + map[y][x + 1] + map[y + 1][x + 1];
		maxSum = maxSum > sum ? maxSum : sum;
	}
	if (y + 2 < n && x + 1 < m) {
		int sum = map[y][x] + map[y + 1][x] + map[y + 2][x] + map[y + 1][x + 1];
		maxSum = maxSum > sum ? maxSum : sum;
	}
	if (y + 1 < n && x - 1 >= 0 && x + 1 < m) {
		int sum = map[y][x] + map[y + 1][x - 1] + map[y + 1][x] + map[y + 1][x + 1];
		maxSum = maxSum > sum ? maxSum : sum;
	}
}

void sol() {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (i + 3 < n || j + 3 < m)
				tetro1(i, j);
			if (i + 1 < n && j + 1 < m)
				tetro2(i, j);
			if (i + 2 < n || i - 1 >= 0 || j + 2 < m || j - 1 >= 0)
				tetro3(i, j);
			if (i + 2 < n || i - 1 >= 0 || j + 2 < m || j - 1 >= 0)
				tetro4(i, j);
			if (i + 2 < n || i - 1 >= 0 || j + 2 < m || j - 1 >= 0)
				tetro5(i, j);
		}
	}
	cout << maxSum;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	input();
	sol();
	return 0;
}