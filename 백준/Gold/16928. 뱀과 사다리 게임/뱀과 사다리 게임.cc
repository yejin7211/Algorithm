#include <iostream>
#include <queue>
#include <cstdbool>

using namespace std;

queue<pair<int,int>> q;
int moveMap[101];
bool visited[101];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n, m;
	cin >> n >> m;
	for (int i = 0; i < n + m; i++) {
		int x, y;
		cin >> x >> y;
		moveMap[x] = y;
	}

	q.push({ 1,0 });
	visited[1] = true;

	while (!q.empty()) {
		int cur = q.front().first;
		int cnt = q.front().second;
		q.pop();
		if (cur == 100) {
			cout << cnt;
			break;
		}

		for (int i = 1; i <= 6; i++) {
			int nextCur = cur + i;
			if (nextCur > 100 || visited[nextCur])
				continue;
			if (moveMap[nextCur] != 0)
				nextCur = moveMap[nextCur];

			q.push({ nextCur,cnt + 1 });
			visited[nextCur] = true;
		}
	}
	return 0;
}