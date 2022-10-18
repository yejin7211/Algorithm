#include <iostream>
#include <queue>

using namespace std;

struct DustInfo {
	int y;
	int x;
	int v;
};

queue<DustInfo> q;
int map[50][50];
int r, c, t;
int cleaner_rIdx = -1;

int dy[4] = { -1,1,0,0 };
int dx[4] = { 0,0,-1,1 };
void show() {
	cout << endl;
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++)
			cout << map[i][j] << ' ';
		cout << endl;
	}
}
void swap(int* a, int* b) {
	int tmp = *a;
	*a = *b;
	*b = tmp;
}
void input() {
	cin >> r >> c >> t;
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			cin >> map[i][j];
			if (map[i][j] == -1)
				cleaner_rIdx = i;
		}
	}
}
void search_dust() {
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			if (map[i][j] > 0) 
				q.push({ i,j,map[i][j] });
		}
	}
}
void move_dust() {
	while (!q.empty()) {
		int y = q.front().y;
		int x = q.front().x;
		int v = q.front().v;
		q.pop();
		
		int moveCnt = 0;
		for (int i = 0; i < 4; i++) {
			int ny = y + dy[i];
			int nx = x + dx[i];

			if (ny < 0 || nx < 0 || ny >= r || nx >= c) continue;
			if (map[ny][nx] != -1) {
				map[ny][nx] += int(v / 5);
				moveCnt++;
			}
		}

		map[y][x] -= int(v / 5) * moveCnt;
	}
}
void operate_airCleaner() {
	int prev = 0;

	// 윗 공기청정기 작동
	cleaner_rIdx -= 1;
	for (int j = 1; j < c; j++) {
		if (map[cleaner_rIdx][j] != 0) {
			if (prev == 0) {
				prev = map[cleaner_rIdx][j];
				map[cleaner_rIdx][j] = 0;
			}
			else swap(&map[cleaner_rIdx][j], &prev);
		}
		else if (map[cleaner_rIdx][j] == 0 && prev != 0) {
			map[cleaner_rIdx][j] = prev;
			prev = 0;
		}
	}

	for (int i = cleaner_rIdx - 1; i >= 0; i--) {
		if (map[i][c - 1] != 0) {
			if (prev == 0) {
				prev = map[i][c - 1];
				map[i][c - 1] = 0;
			}
			else swap(&map[i][c - 1], &prev);
		}
		else if (map[i][c - 1] == 0 && prev != 0) {
			map[i][c - 1] = prev;
			prev = 0;
		}
	}

	for (int j = c - 2; j >= 0; j--) {
		if (map[0][j] != 0) {
			if (prev == 0) {
				prev = map[0][j];
				map[0][j] = 0;
			}
			else swap(&map[0][j], &prev);
		}
		else if (map[0][j] == 0 && prev != 0) {
			map[0][j] = prev;
			prev = 0;
		}
	}

	for (int i = 1; i < cleaner_rIdx; i++) {
		if (map[i][0] != 0) {
			if (prev == 0) {
				prev = map[i][0];
				map[i][0] = 0;
			}
			else swap(&map[i][0], &prev);
		}
		else if (map[i][0] == 0 && prev != 0) {
			map[i][0] = prev;
			prev = 0;
		}
	}

	prev = 0;
	// 아래 공기청정기 작동
	cleaner_rIdx += 1;
	for (int j = 1; j < c; j++) {
		if (map[cleaner_rIdx][j] != 0) {
			if (prev == 0) {
				prev = map[cleaner_rIdx][j];
				map[cleaner_rIdx][j] = 0;
			}
			else swap(&map[cleaner_rIdx][j], &prev);
		}
		else if (map[cleaner_rIdx][j] == 0 && prev != 0) {
			map[cleaner_rIdx][j] = prev;
			prev = 0;
		}
	}

	for (int i = cleaner_rIdx + 1; i < r; i++) {
		if (map[i][c - 1] != 0) {
			if (prev == 0) {
				prev = map[i][c - 1];
				map[i][c - 1] = 0;
			}
			else swap(&map[i][c - 1], &prev);
		}
		else if (map[i][c - 1] == 0 && prev != 0) {
			map[i][c - 1] = prev;
			prev = 0;
		}
	}

	for (int j = c - 2; j >= 0; j--) {
		if (map[r - 1][j] != 0) {
			if (prev == 0) {
				prev = map[r - 1][j];
				map[r - 1][j] = 0;
			}
			else swap(&map[r - 1][j], &prev);
		}
		else if (map[r - 1][j] == 0 && prev != 0) {
			map[r - 1][j] = prev;
			prev = 0;
		}
	}

	for (int i = r - 2; i > cleaner_rIdx; i--) {
		if (map[i][0] != 0) {
			if (prev == 0) {
				prev = map[i][0];
				map[i][0] = 0;
			}
			else swap(&map[i][0], &prev);
		}
		else if (map[i][0] == 0 && prev != 0) {
			map[i][0] = prev;
			prev = 0;
		}
	}
}
void reset() {
	q = queue<DustInfo>();
}
int search_totalDust() {
	int sum = 0;
	for (int i = 0; i < r; i++)
		for (int j = 0; j < c; j++)
			if (map[i][j] != -1)
				sum += map[i][j];
	return sum;
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	input();
	while (t--) {
		search_dust();
		move_dust();
		operate_airCleaner();
		reset();
	}
	cout << search_totalDust();
	return 0;
}