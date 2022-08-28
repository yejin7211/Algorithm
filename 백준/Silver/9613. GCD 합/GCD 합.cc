#include <stdio.h>
long long n[100];

long long solution(long long a, long long b) {
	if (b == 0) return a;
	else return solution(b, a % b);
}
int main() {
	long long T;
	scanf("%lld", &T);

	long long N;
	for (long long i = 0; i < T; i++) {
		scanf("%lld", &N);
		for (long long j = 0; j < N; j++)
			scanf("%lld", &n[j]);

		long long sum = 0;
		for (long long m = 0; m < N; m++) {
			for (long long k = m + 1; k < N; k++) 
				sum += solution(n[m], n[k]);
		}

		printf("%lld\n", sum);
	}
	return 0;
}