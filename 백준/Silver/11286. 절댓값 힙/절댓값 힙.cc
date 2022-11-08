#include <iostream>
#include <queue>
#include <cmath>

using namespace std;

typedef pair<double, int> P; // 절댓값, 절댓값 적용 여부
priority_queue<P, vector<P>, greater<P>> pq;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n, x;
	cin >> n;
	while (n--) {
		cin >> x;
		if (x == 0) {
			if (pq.empty()) cout << 0 << '\n';
			else {
				int v = pq.top().first;
				int check = pq.top().second;
				if (check) cout << (v + 1) * -1 << '\n';
				else cout << v << '\n';
				pq.pop();
			}
		}
		else {
			if (x > 0) pq.push({ x, 0 });
			else pq.push({ -1 * x - 0.5, 1 });
		}
	}
	return 0;
}