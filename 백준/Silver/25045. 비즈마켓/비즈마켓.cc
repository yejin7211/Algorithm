#include <stdio.h>
#include <stdlib.h>
long long A[200000];
long long B[200000];

int compareup(const void* a, const void* b) {
	return *(long long*)a - *(long long*)b;
}
int comparedown(const void* a, const void* b) {
	return *(long long*)b - *(long long*)a;
}

int main() {
	long long N, M;
	scanf("%lld %lld", &N, &M);
	for (long long i = 0; i < N; i++)
		scanf("%lld", &A[i]);
	for (int i = 0; i < M; i++)
		scanf("%lld", &B[i]);

	qsort(A, N, sizeof(long long), comparedown);
	qsort(B, M, sizeof(long long), compareup);

	long long total = 0;
	long long aIdx = 0;
	long long bIdx = 0;
	while (bIdx < M && aIdx < N) {
		if (A[aIdx] >= B[bIdx])
			total += A[aIdx++] - B[bIdx++];
		else bIdx++;
	}

	printf("%lld", total);
	return 0;
}