#include <stdio.h>
#include <stdlib.h>
typedef struct {
	int m;
	int n;
}Grade;
Grade grade[100000];

int compare(const void* a, const void* b) {
	Grade* pA = (Grade*)a;
	Grade* pB = (Grade*)b;

	return pA->m - pB->m;
}
int main() {
	int T;
	scanf("%d", &T);

	int N;
	for (int i = 0; i < T; i++) {
		scanf("%d", &N);
		
		for (int j = 0; j < N; j++) 
			scanf("%d %d", &grade[j].m, &grade[j].n);
		
		qsort(grade, N, sizeof(Grade), compare);

		int cnt = 0;
		int min = grade[0].n;
		for (int j = 1; j < N; j++) {
			if (grade[j].n > min) cnt++;
			else if (grade[j].n < min) min = grade[j].n;
		}

		printf("%d\n", N - cnt);
	}

	return 0;
}