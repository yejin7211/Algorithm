#include <stdio.h>
typedef long long ll;
ll F[1000000];

int main() {
	int n;
	scanf("%d", &n);

	F[0] = 0;
	F[1] = 1;
	for (ll i = 2; i <= n; i++)
		F[i] = (F[i - 1] + F[i - 2]) % 1000000007;

	printf("%lld", F[n]);

	return 0;
}