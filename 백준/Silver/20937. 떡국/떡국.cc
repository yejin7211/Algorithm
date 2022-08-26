#include <stdio.h>
#include <stdlib.h>
int c[500000];
int num[500001];

int compare(const void* a, const void* b) {
	return *(int*)b - *(int*)a;
}
int main() {
	int N;
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		scanf("%d", &c[i]);
		num[c[i]]++;
	}

	int max = -1;
	for (int i = 1; i < 500001; i++) {
		if (num[i] == 0) continue;
		max = max > num[i] ? max : num[i];
	}
	printf("%d", max);
	return 0;
}

//4 4 3 3 2 2 1 1