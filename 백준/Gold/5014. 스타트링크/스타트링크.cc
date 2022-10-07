#include <iostream>
#include <cstdbool>
#include <vector>
#include <queue>
#define MAX 1000001

using namespace std;

priority_queue<pair<int, int>, vector<pair<int, int>>,
	greater<pair<int, int>>> pq;
bool visited[MAX];
int f, s, g, u, d;

int bfs() {
	pq.push({ s,0 });
	visited[s] = true;

	while (!pq.empty()) {
		s = pq.top().first;
		int l = pq.top().second;
		pq.pop();

		if (s == g) 
			return l;

		if (s + u < MAX && s + u <= f && !visited[s + u]) {
			pq.push({ s + u,l + 1 });
			visited[s + u] = true;
		}
		if (s - d >= 1 && !visited[s - d]) {
			pq.push({ s - d,l + 1 });
			visited[s - d] = true;
		}
	}
	return -1;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> f >> s >> g >> u >> d;
	int ans = bfs();
	if (ans == -1) cout << "use the stairs";
	else cout << ans;
	return 0;
}  