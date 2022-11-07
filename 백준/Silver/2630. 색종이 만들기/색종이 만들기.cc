#include <iostream>

using namespace std;

int n;
int map[128][128];
int cnt[2]; // 햐얀색, 파란색 색종이의 개수

void input() {
	cin >> n;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			cin >> map[i][j];
}

// 전체 종이가 모두 같은 색으로 칠해져 있는지 확인하는 함수
int isAllSame(int y, int x, int size) {
	for (int i = y; i < y + size; i++)
		for (int j = x; j < x + size; j++)
			if (map[i][j] != map[y][x])
				return 0;
	return 1;
}

void sol(int y, int x, int size) {
	if (isAllSame(y, x, size))  // 전체 종이가 모두 같은 색으로 칠해져 있는지 확인
		cnt[map[y][x]]++; // 모두 같은 색이라면 해당 색종이의 개수 세기
	else { // 색종이 4등분
		sol(y, x, size / 2);
		sol(y, x + size / 2, size / 2);
		sol(y + size / 2, x, size / 2);
		sol(y + size / 2, x + size / 2, size / 2);
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	input();
	sol(0, 0, n);
	cout << cnt[0] << '\n' << cnt[1];
	return 0;
}