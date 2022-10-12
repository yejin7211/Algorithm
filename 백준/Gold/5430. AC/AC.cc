#include <iostream>
#include <deque>
#include <string>

using namespace std;

deque<int> d;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int t, n, i, rev, errored;
	string p, arr;
	cin >> t;
	while (t--) {
		cin >> p;
		cin >> n;
		cin >> arr;

		i = 1;
		while (i < arr.length() - 1) {
			if ('0' <= arr[i] && arr[i] <= '9') {
				d.push_back(atoi(&arr[i]));
				while ('0' <= arr[i] && arr[i] <= '9' && i < arr.length() - 1)
					i++;
			}
			else i++;
		}
	
		rev = 0;
		errored = 0;
		i = 0;
		while (i < p.length()) {
			if (p[i] == 'R') {
				rev++;
				i++;
				while (p[i] == 'R' && i < p.length()) {
					rev++;
					i++;
				}
			}
			else if (p[i] == 'D') {
				if (d.empty()) {
					errored = 1;
					cout << "error" << '\n';
					break;
				}
				if (rev % 2 == 1) d.pop_back();
				else d.pop_front();
				i++;
			}
		}

		if (!errored) {
			int Size = d.size();
			cout << "[";
			if (rev % 2 == 1) {
				for (i = 0; i < Size; i++) {
					cout << d.back();
					d.pop_back();
					if (i != Size - 1) cout << ",";
				}
			}
			else {
				for (i = 0; i < Size; i++) {
					cout << d.front();
					d.pop_front();
					if (i != Size - 1) cout << ",";
				}
			}
			cout << "]" << '\n';
		}
	}
	return 0;
}