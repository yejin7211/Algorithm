#include <iostream>
#include <cstdlib>
#include <cstring>
using namespace std;

typedef struct {
	char name[21];
}NoHear;
NoHear nh[500000];

typedef struct {
	char name[21];
}NoHearSee;
NoHearSee nhs[500000];

int compare(const void* a, const void* b) {
	NoHear pA = *(NoHear*)a;
	NoHear pB = *(NoHear*)b;
	return strcmp(pA.name, pB.name);
}

int binarysearch(int start, int end, char target[20]) {
	while (start <= end) {
		int mid = (start + end) / 2;
		if (strcmp(target, nh[mid].name) == 0) return 1;
		else if (strcmp(target, nh[mid].name) < 0) end = mid - 1;
		else start = mid + 1;
	}
	return 0;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n, m;
	cin >> n >> m;
	for (int i = 0; i < n; i++)
		cin >> nh[i].name;

	qsort(nh, n, sizeof(NoHear), compare);

	int cnt = 0;
	for (int i = 0; i < m; i++) {
		char name[21];
		cin >> name;
		if (binarysearch(0, n - 1, name) == 1) 
			strcpy(nhs[cnt++].name, name);
	}

	qsort(nhs, cnt, sizeof(NoHearSee), compare);

	cout << cnt << '\n';
	for (int i = 0; i < cnt; i++)
		cout << nhs[i].name << '\n';
	return 0;
}