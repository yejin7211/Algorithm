#include <iostream>
#include <cstdbool>
#include <queue>
#include <vector>
#include <cmath>

using namespace std;

int map[50][50];
bool opened[50][50];
queue<pair<int, int>> q;
vector<pair<int, int>> v;
int total_population = 0;
int n, l, r;

int dy[4] = { -1,1,0,0 };
int dx[4] = { 0,0,-1,1 };

void input() {
	cin >> n >> l >> r;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			cin >> map[i][j];
}

int openLines(int y, int x) {
	total_population = map[y][x];
	int countryCnt = 1;

	q.push({ y,x });
	while (!q.empty()) {
		int y = q.front().first;
		int x = q.front().second;
		q.pop();

		for (int i = 0; i < 4; i++) {
			int ny = y + dy[i];
			int nx = x + dx[i];

			if (ny < 0 || nx < 0 || ny >= n || nx >= n) continue;
			if (!opened[ny][nx] && l <= abs(map[y][x]-map[ny][nx]) && abs(map[y][x] - map[ny][nx]) <= r) {
				q.push({ ny,nx });
				v.push_back({ ny,nx });
				opened[y][x] = true;
				opened[ny][nx] = true;
				total_population += map[ny][nx];
				countryCnt++;
			}
		}
	}
	return countryCnt;
}

void movePopulation(int population) {
	while (!v.empty()) {
		int y = v.back().first;
		int x = v.back().second;
		v.pop_back();
		map[y][x] = population;
	}
}

int movedPopulation() {
	// 조건에 맞는 국경선이 열리면 인구 이동
	int flag = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (!opened[i][j]) {
				int countryCnt = openLines(i, j);
				if (countryCnt != 1) {
					v.push_back({ i,j });
					int population = int(total_population / countryCnt);
					movePopulation(population);
					flag = 1;
				}
			}
		}
	}
	return flag;
}

void closeLines() {
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			opened[i][j] = false;
}

void solution() {
	int date = 0;
	while (1) {
		if (movedPopulation()) date++;
		else break;
		closeLines();
	}
	cout << date;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	input();
	solution();
	return 0;
}