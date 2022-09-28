#include <iostream>
#include <cstdbool>
#include <vector>
#include <queue>
using namespace std;
bool visited[100001];

int main() {
	int n, k;
	cin >> n >> k;

	queue<pair<int, int>> q;
	q.emplace(n, 0);

	while (!q.empty()) {
		int pos = q.front().first;
		int cnt = q.front().second;
		q.pop();

		if (pos == k) {
			cout << cnt;
			break;
		}

		if (0 <= pos - 1 && !visited[pos - 1]) {
			visited[pos - 1] = true;
			q.emplace(pos - 1, cnt + 1);
		}
		if (pos + 1 <= 100000 && !visited[pos + 1]) {
			visited[pos + 1] = true;
			q.emplace(pos + 1, cnt + 1);
		}
		if (pos * 2 <= 100000 && !visited[pos * 2]) {
			visited[pos * 2] = true;
			q.emplace(pos * 2, cnt + 1);
		}
	}
	return 0;
}