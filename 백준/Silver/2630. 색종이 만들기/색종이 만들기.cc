#include <iostream>
#include <cstdbool>

using namespace std;

int map[128][128];
int colorCnt[2];
int paperCnt[2];
int n;

// 해당 범위내 색깔이 모두 color와 같은지 확인
bool isPossible(int r, int c, int len, int color) {
	for (int i = r; i < r + len; i++)
		for (int j = c; j < c + len; j++)
			if (map[i][j] != color)
				return false;

	return true;
}

void divideArea(int r, int c, int len, int color) {
	if (len == 1) { // 1개짜리면
		if (map[r][c] == color) { //색이 같다면 색종이+1 && 색깔 수-1
			colorCnt[color]--;
			paperCnt[color]++;
		}
	}
	else {
		int check[2] = { 0,len / 2 };

		for (int i = 0; i < 2; i++) {  // 4등분
			for (int j = 0; j < 2; j++) {
				if (isPossible(r + check[i], c + check[j], len / 2, color)) { //색이 같다면
					colorCnt[color] -= (len / 2) * (len / 2);
					paperCnt[color]++;
					if (colorCnt[color] == 0) return; //모든 해당 color 확인시 돌아가기
				}
				else divideArea(r + check[i], c + check[j], len / 2, color); //아니라면 다시 4등분
			}
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	// 입력
	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> map[i][j];
			colorCnt[map[i][j]]++; //흰색과 파랑색 세기
		}
	}

	for (int i = 0; i < 2; i++) {
		if (isPossible(0, 0, n, i)) paperCnt[i]++; //모두 해당색으로 같다면 색종이+1
		else divideArea(0, 0, n, i); // 그렇지 않다면 4등분
		cout << paperCnt[i] << '\n'; // 색종이 수 출력
	}
	return 0;
} 