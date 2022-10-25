#include <iostream>
#define MAX(a, b) ( (a)>(b)?(a):(b) )
#define MIN(a, b) ( (a)<(b)?(a):(b) )

using namespace std;

int n;
int map[100000][3];

void input() {
	cin >> n;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < 3; j++)
			cin >> map[i][j];
}

void sol() {
	// 최대 점수 구하기
	int scores[3] = { map[0][0], map[0][1], map[0][2] };

	int n0, n1, n2;
	for (int i = 1; i < n; i++) {
		n0 = map[i][0] +  MAX(scores[0], scores[1]);
		n1 = map[i][1] + MAX(MAX(scores[0], scores[1]), scores[2]);
		n2 = map[i][2] + MAX(scores[1], scores[2]);
		scores[0] = n0;
		scores[1] = n1;
		scores[2] = n2;
	}
	cout << MAX(MAX(scores[0], scores[1]), scores[2]) << ' ';

	// 최소 점수 구하기
	for (int i = 0; i < 3; i++)
		scores[i] = map[0][i];

	for (int i = 1; i < n; i++) {
		n0 = map[i][0] + MIN(scores[0], scores[1]);
		n1 = map[i][1] + MIN(MIN(scores[0], scores[1]), scores[2]);
		n2 = map[i][2] + MIN(scores[1], scores[2]);
		scores[0] = n0;
		scores[1] = n1;
		scores[2] = n2;
	}
	cout << MIN(MIN(scores[0], scores[1]), scores[2]);
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	input();
	sol();
	return 0;
}