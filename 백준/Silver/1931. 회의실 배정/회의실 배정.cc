#include <stdio.h>
#include <stdlib.h>
typedef struct {
	int s;
	int e;
}Time;
Time T[100000];
int N;

int compare(const void* a, const void* b) {
	if (((Time*)a)->e == ((Time*)b)->e) 
		return ((Time*)a)->s - ((Time*)b)->s;
	return ((Time*)a)->e - ((Time*)b)->e;
}

int main() {
	scanf("%d", &N);
	for (int i = 0; i < N; i++)
		scanf("%d %d", &T[i].s, &T[i].e);

	qsort((Time*)T, N, sizeof(Time), compare);

	int cnt = 1;
	int tmp = T[0].e;
	for (int i = 1; i < N; i++) {
		if (tmp <= T[i].s) {
			cnt++;
			tmp = T[i].e;
		}
	}

	printf("%d", cnt);
	return 0;
}