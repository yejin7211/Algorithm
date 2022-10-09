#include <iostream>

using namespace std;

char s[1000001];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n, m;
	int cnt = 0;
	cin >> n;
	cin >> m;
	cin >> s;

	for (int i = 0; i < m; i++) {
		if (s[i] == 'I') {
			int count = 0;
			while (s[i + 1] == 'O' && s[i + 2] == 'I') {
				count++;
				if (count == n) {
					count--;
					cnt++;
				}
				i += 2;
			}
		}
	}
	cout << cnt;
	return 0;
}