#include <iostream>
#include <cstdlib>
using namespace std;
struct Meeting {
	int s;
	int e;
	int p;
};
Meeting arrM[25];

int compare(const void* a, const void* b) {
	Meeting* pA = (Meeting*)a;
	Meeting* pB = (Meeting*)b;

	return pA->s - pB->s;
}
int main() {
	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
		cin >> arrM[i].s >> arrM[i].e >> arrM[i].p;

	qsort(arrM, n, sizeof(Meeting), compare);

	int maxMember = 0;
	for (int i = n - 1; i >= 0; i--) {
		int maxP = 0;
		for (int j = i + 1; j < n; j++) {
			if (arrM[i].e <= arrM[j].s)
				maxP = maxP > arrM[j].p ? maxP : arrM[j].p;
		}
		arrM[i].p += maxP;
		maxMember = maxMember > arrM[i].p ? maxMember : arrM[i].p;
	}
	cout << maxMember;
	return 0;
}