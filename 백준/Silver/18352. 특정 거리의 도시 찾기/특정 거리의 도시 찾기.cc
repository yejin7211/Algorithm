#include <iostream>
#include <cstdbool>
#include <queue>
#include <vector>

using namespace std;

int n, m, k, x;
vector<int> city[300001];
bool visited[300001];
queue<int> q;
int level[300001];

void bfs(int x) {
	visited[x] = true;
	while (!city[x].empty()) {
		if (!visited[city[x].back()]) {
			q.push(city[x].back());
			visited[city[x].back()] = true;
			level [city[x].back()] = level[x] + 1;
		}
		city[x].pop_back();
	}

	while (!q.empty()) {
		x = q.front();
		q.pop();

		while (!city[x].empty()) {
			if (!visited[city[x].back()]) {
				q.push(city[x].back());
				visited[city[x].back()] = true;
				level[city[x].back()] = level[x] + 1;
			}
			city[x].pop_back();
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n >> m >> k >> x;
	while (m--) {
		int a, b;
		cin >> a >> b;
		city[a].push_back(b);
	}

	bfs(x);

	int flag = 0;
	for (int i = 1; i <= n; i++) {
		if (level[i] == k) {
			flag = 1;
			cout << i << '\n';
		}
	}

	if (!flag) cout << -1;
	return 0;
}