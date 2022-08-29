#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int n[200000];

int compare(const void* a, const void* b) {
	return *(int*)a - *(int*)b;
}
int main() {
	int N;
	scanf("%d", &N);
	for (int i = 0; i < N; i++)
		scanf("%d", &n[i]);

	qsort(n, N, sizeof(int), compare);

	if (N % 2 == 0) {
		int pos1 = n[(N / 2) - 1];
		int pos2 = n[(N / 2)];

		long long sum1 = 0;
		for (int i = 0; i < N; i++) 
			sum1 += abs(pos1 - n[i]);

		long long sum2 = 0;
		for (int i = 0; i < N; i++)
			sum2 += abs(pos2 - n[i]);
		
		if (sum1 <= sum2) printf("%d", pos1);
		else printf("%d", pos2);
	}
	else {
		int pos = n[(N - 1) / 2];

		long long sum = 0;
		for (int i = 0; i < N; i++) 
			sum += abs(pos - n[i]);

		printf("%d", pos);
	}

	return 0;
}