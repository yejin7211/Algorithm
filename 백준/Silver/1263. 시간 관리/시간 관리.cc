#include <stdio.h>
#include <stdlib.h>
typedef struct {
	int t;
	int s;
}Work;
Work work[1000];
int MAX = 1000000;

int compare(const void* a, const void* b) {
	Work* pA = (Work*)a;
	Work* pB = (Work*)b;

	if (pA->s == pB->s) return pA->t - pB->t;
	else return pA->s - pB->s;
}
int main() {
	int N;
	scanf("%d", &N);
	for (int i = 0; i < N; i++)
		scanf("%d %d", &work[i].t, &work[i].s);

	qsort(work, N, sizeof(Work), compare);

	int time = 0;
	int min = MAX;
	for (int i = 0; i < N; i++) {
		time += work[i].t;
		if (time > work[i].s) {
			printf("-1");
			return 0;
		}

		min = min < work[i].s - time ? min : work[i].s - time;
	}

	printf("%d", min);

	return 0;
}