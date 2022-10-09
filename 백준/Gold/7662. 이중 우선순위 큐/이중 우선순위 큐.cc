#include <iostream>
#include <set>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int t;
	cin >> t;
	while (t--) {
		int k;
		cin >> k;

		multiset<int> ms;
		while (k--) {
			char c;
			int n;
			cin >> c >> n;
			if (c == 'I')
				ms.insert(n);
			else {
				if (!ms.empty() && n == 1) {
					auto iter = ms.end();
					ms.erase(--iter);
				}
				else if (!ms.empty() && n == -1) 
					ms.erase(ms.begin());
			}
		}

		if (ms.empty()) cout << "EMPTY" << '\n';
		else {
			auto iter = ms.end();
			iter--;
			cout << *iter << ' ' << *ms.begin() << '\n';
		}
	}
	return 0;
}