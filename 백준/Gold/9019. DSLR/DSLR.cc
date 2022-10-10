#include <iostream>
#include <cstring>
#include <cstdbool>
#include <queue>

using namespace std;

bool visited[10000];
int a, b;

void bfs() {
	queue<pair<int, string>> q;
	q.push(make_pair(a, "")); //처음 값 넣기
	visited[a] = true;

	while (!q.empty()) {
		int n = q.front().first;
		string str = q.front().second;
		q.pop();

		if (n == b) {
			cout << str << '\n';
			break;
		}

		//D: D 는 n을 두 배로 바꾼다.
		int D = (n * 2) % 10000;
		if (!visited[D]) {
			visited[D] = true;
			q.push({ D,str + 'D' });
		}

		//S: S 는 n에서 1 을 뺀 결과 n-1을 레지스터에 저장한다.
		int S = n == 0 ? 9999 : n - 1;
		if (!visited[S]) {
			visited[S] = true;
			q.push({ S,str + 'S' });
		}
		

		//L: L 은 n의 각 자릿수를 왼편으로 회전시켜 그 결과를 레지스터에 저장한다.
		int L= (n % 1000) * 10 + (n / 1000);
		if (!visited[L]) {
			visited[L] = true;
			q.push({ L,str + 'L' });
		}

		//R: R 은 n의 각 자릿수를 오른편으로 회전시켜 그 결과를 레지스터에 저장한다.
		int R = (n / 10) + (n % 10) * 1000;
		if (!visited[R]) {
			visited[R] = true;
			q.push({ R,str + 'R' });
		}
	}
}

void init() {
	for (int i = 0; i < 10000; i++) 
		visited[i] = false;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	// 입력
	int t;
	cin >> t;
	while (t--) {
		cin >> a >> b;
		bfs(); //너비 우선 탐색
		init(); //초기화
	}
	return 0;
}