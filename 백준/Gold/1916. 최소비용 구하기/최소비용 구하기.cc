#include <iostream>
#include <queue>
#define INF 987654321

using namespace std;

int n, m, s, e;
int dist[1001];
vector<pair<int, int>> v[1001];

void input() {
	cin >> n >> m;
	while (m--) {
		int a, b, c;
		cin >> a >> b >> c;
		v[a].push_back({ b, c });
	}
	cin >> s >> e;

	for (int i = 1; i <= n; i++)
		dist[i] = INF;
}

void Dijkstra() {
	typedef pair<int, int> P; //비용, 현재 위치
	priority_queue<P, vector<P>, greater<P>> pq; // 최소 힙

	pq.push({ 0,s });
	dist[s] = 0;

	while (!pq.empty()) {
		int money = pq.top().first;
		int cur = pq.top().second;
		pq.pop();

		if (dist[cur] < money) continue;
		for (int i = 0; i < v[cur].size(); i++) {
			int nextCur = v[cur][i].first;
			int nextMoney = dist[cur] + v[cur][i].second;
			if (nextMoney < dist[nextCur]) {
				dist[nextCur] = nextMoney;
				pq.push({ nextMoney, nextCur });
			}
		}
	}
	cout << dist[e];
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	input();
	Dijkstra();
	return 0;
}