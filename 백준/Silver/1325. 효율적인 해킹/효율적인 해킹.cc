#include <iostream>
#include <cstdbool>
#include <queue>
using namespace std;

vector<int> map[10001];
bool visited[10001];
queue<int> q;
vector<pair<int, int>> v;
int n, m;
int hacked = 1;

void input() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n >> m;
	while (m--) {
		int a, b;
		cin >> a >> b;
		map[b].push_back(a);
	}
}

void init() {
	hacked = 1;
	for (int i = 1; i <= n; i++)
		visited[i] = false;
}

void func(int v) {
	visited[v] = true;
	q.push(v);

	while (!q.empty()) {
		v = q.front();
		q.pop();

		for (int w = 0; w < map[v].size(); w++) {
			int nv = map[v][w];

			if (visited[nv] == 0) {
				visited[nv] = true;
				q.push(nv);
				hacked++;
			}
		}
	}
}

void sol() {
	for (int i = 1; i <= n; i++) {
		func(i);
		v.push_back(make_pair(i, hacked));
		init();
	}
	
	int maxHack = -1;
	for (int i = 0; i < v.size(); i++) 
		maxHack = maxHack > v[i].second ? maxHack : v[i].second;

	for (int i = 0; i < v.size(); i++) {
		if (v[i].second == maxHack)
			cout << v[i].first << ' ';
	}
}

int main() {
	input();
	sol();
	return 0;
}