#include <iostream>
#include <queue>

using namespace std;

bool visited[100001];
int cnt = 0;
int minT = 987654321;
int n, k;

void input() {
	cin >> n >> k;
}

void bfs() {
	queue<pair<int, int>> q;

	q.push({ 0,n });
	visited[n] = true;
	while (!q.empty()) {
		int time = q.front().first;
		int pos = q.front().second;
		q.pop();

		visited[pos] = true;

		if (pos == k) {
			if (minT == 987654321) {
				minT = time;
				cnt++;
			}
			else if (time == minT)
				cnt++;
			continue;
		}

		if (pos - 1 >= 0 && !visited[pos - 1])
			q.push({ time + 1, pos - 1 });
		if (pos + 1 < 100001 && !visited[pos + 1])
			q.push({ time + 1, pos + 1 });
		if (pos * 2 < 100001 && !visited[pos * 2])
			q.push({ time + 1, pos * 2 });
	}
}

void sol() {
	bfs();
	cout << minT << '\n';
	cout << cnt;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	input();
	sol();
	return 0;
}