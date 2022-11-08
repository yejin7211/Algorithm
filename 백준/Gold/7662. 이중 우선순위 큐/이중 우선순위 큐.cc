#include <iostream>
#include <set>

using namespace std;

/*
multiset
- 내장함수: set
- set: 중복을 없앰. 입력 시 정렬이 되며 입력됨
- set과 비슷하나, multiset은 중복을 허용
- 기본적으로 오름차순 정렬, greater로 내림차순 정렬 가능
- intert, clear, begin(), end(), count(n), size()
*/

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int t, k, n;
	char c;
	cin >> t;
	while (t--) {
		multiset<int> ms; // default: 오름차순 정렬
		cin >> k;
		while (k--) {
			cin >> c >> n;
			if (c == 'I') 
				ms.insert(n);
			else {
				if (ms.empty())
					continue;
				if (n == -1) ms.erase(ms.begin()); // 가장 앞 위치 삭제
				else {
					auto iter = ms.end(); 
					ms.erase(--iter); // 가장 뒤 원소가 있는 위치 삭제
				}
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