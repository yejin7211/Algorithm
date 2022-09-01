#include <stdio.h>
#include <math.h>
int A[100000];
int L[100000];

int gcd(int x, int y) {
	if (y == 0) return x;
	else return gcd(y, x % y);
}
int main() {
	int N, S;
	scanf("%d %d", &N, &S);
	for (int i = 0; i < N; i++) {
		scanf("%d", &A[i]);
		L[i] = abs(A[i] - S);
	}

	int ans = L[0];
	for (int i = 1; i < N; i++) {
		ans = gcd(ans, L[i]);
	}

	printf("%d", ans);
	return 0;
}