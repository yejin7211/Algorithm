#include <iostream>
#include <queue>
using namespace std;

struct ConnectedNodes {
	queue<int> q;
};
ConnectedNodes nodes[100001];
queue<int> nq;
int ans[100001];

void sol() {
	while (!nq.empty()) {
		int parent = nq.front();
		nq.pop();
		while (!nodes[parent].q.empty()) {
			int child = nodes[parent].q.front();
			nodes[parent].q.pop();
			if (child != 1 && ans[child] == 0) {
				nq.push(child);
				ans[child] = parent;
			}
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	int n;
	cin >> n;
	int input = n - 1;
	while (input--) {
		int a, b;
		cin >> a >> b;

		nodes[a].q.push(b);
		nodes[b].q.push(a);

		if (a == 1) {
			nq.push(b);
			ans[b] = 1;
		}
		if (b == 1) {
			nq.push(a);
			ans[a] = 1;
		}
	}
	sol();

	for (int i = 2; i <= n; i++)
		cout << ans[i] << '\n';
	return 0;
}