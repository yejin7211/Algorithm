#include <iostream>
#define MAX(a, b) ( (a)>(b)?(a):(b) )

using namespace std;

int n, m;
int map[500][500];

void input() {
	cin >> n >> m;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			cin >> map[i][j];
}

int tetro1_1(int y, int x) {
	return map[y][x] + map[y][x + 1] + map[y][x + 2] + map[y][x + 3];
}
int tetro1_2(int y, int x) {
	return map[y][x] + map[y + 1][x] + map[y + 2][x] + map[y + 3][x];
}

int tetro2(int y, int x) {
	return map[y][x] + map[y][x + 1] + map[y + 1][x] + map[y + 1][x + 1];
}

int tetro3_1(int y, int x) {
	return map[y][x] + map[y + 1][x] + map[y + 2][x] + map[y + 2][x + 1];
}
int tetro3_2(int y, int x) {
	return map[y][x] + map[y][x + 1] + map[y][x + 2] + map[y + 1][x];
}
int tetro3_3(int y, int x) {
	return map[y][x] + map[y][x + 1] + map[y + 1][x + 1] + map[y + 2][x + 1];
}
int tetro3_4(int y, int x) {
	return map[y][x] + map[y][x + 1] + map[y][x + 2] + map[y - 1][x + 2];
}
int tetro3_5(int y, int x) {
	return map[y][x] + map[y][x + 1] + map[y - 1][x + 1] + map[y - 2][x + 1];
}
int tetro3_6(int y, int x) {
	return map[y][x] + map[y][x + 1] + map[y][x + 2] + map[y + 1][x + 2];
}
int tetro3_7(int y, int x) {
	return map[y][x] + map[y][x + 1] + map[y + 1][x] + map[y + 2][x];
}
int tetro3_8(int y, int x) {
	return map[y][x] + map[y + 1][x] + map[y + 1][x + 1] + map[y + 1][x + 2];
}

int tetro4_1(int y, int x) {
	return map[y][x] + map[y + 1][x] + map[y + 1][x + 1] + map[y + 2][x + 1];
}
int tetro4_2(int y, int x) {
	return map[y][x] + map[y][x + 1] + map[y + 1][x + 1] + map[y + 1][x + 2];
}
int tetro4_3(int y, int x) {
	return map[y][x] + map[y + 1][x] + map[y + 1][x - 1] + map[y + 2][x - 1];
}
int tetro4_4(int y, int x) {
	return map[y][x] + map[y][x + 1] + map[y + 1][x] + map[y + 1][x - 1];
}

int tetro5_1(int y, int x) {
	return map[y][x] + map[y][x + 1] + map[y][x + 2] + map[y + 1][x + 1];
}
int tetro5_2(int y, int x) {
	return map[y][x] + map[y][x + 1] + map[y][x + 2] + map[y - 1][x + 1];
}
int tetro5_3(int y, int x) {
	return map[y][x] + map[y + 1][x] + map[y + 2][x] + map[y + 1][x + 1];
}
int tetro5_4(int y, int x) {
	return map[y][x] + map[y][x + 1] + map[y - 1][x + 1] + map[y + 1][x + 1];
}

void sol() {
	int maxSum = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (j + 3 < m) maxSum = MAX(tetro1_1(i, j), maxSum);
			if (i + 3 < n) maxSum = MAX(tetro1_2(i, j), maxSum);
			if (i + 1 < n && j + 1 < m) maxSum = MAX(tetro2(i, j), maxSum);
			if (i + 2 < n && j + 1 < m) {
				maxSum = MAX(tetro3_1(i, j), maxSum);
				maxSum = MAX(tetro3_3(i, j), maxSum);
				maxSum = MAX(tetro3_7(i, j), maxSum);
				maxSum = MAX(tetro4_1(i, j), maxSum);
				maxSum = MAX(tetro5_3(i, j), maxSum);
			}
			if (i + 1 < n && j + 2 < m) {
				maxSum = MAX(tetro3_2(i, j), maxSum);
				maxSum = MAX(tetro3_6(i, j), maxSum);
				maxSum = MAX(tetro3_8(i, j), maxSum);
				maxSum = MAX(tetro4_2(i, j), maxSum);
				maxSum = MAX(tetro5_1(i, j), maxSum);
			}
			if (i - 1 >= 0 && j + 2 < m) {
				maxSum = MAX(tetro3_4(i, j), maxSum);
				maxSum = MAX(tetro5_2(i, j), maxSum);
			}
			if (i - 2 >= 0 && j + 1 < m)  maxSum = MAX(tetro3_5(i, j), maxSum);
			if (i + 2 < n && j - 1 >= 0)  maxSum = MAX(tetro4_3(i, j), maxSum);
			if (i + 1 < n && j - 1 >= 0 && j + 1 < m)  maxSum = MAX(tetro4_4(i, j), maxSum);
			if (i - 1 >= 0 && i + 1 < n && j + 1 < m) maxSum = MAX(tetro5_4(i, j), maxSum);
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