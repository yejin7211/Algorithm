#include <stdio.h>
#include <stdlib.h>
typedef struct {
	int idx;
	int time;
}Person;
Person p[1000];

int compare(const void* a, const void* b) {
	Person pA = *(Person*)a;
	Person pB = *(Person*)b;

	return pA.time - pB.time;
}

int main() {
	int N;
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		scanf("%d", &p[i].time);
		p[i].idx = i;
	}

	qsort(p, N, sizeof(Person), compare);

	int total = 0;
	for (int i = 0; i < N; i++) {
		total += p[i].time * (N - i);
	}

	printf("%d", total);

	return 0;
}