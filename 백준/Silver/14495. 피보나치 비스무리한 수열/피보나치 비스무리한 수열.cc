#include <stdio.h>
typedef long long ll;
ll f[117];

int main() {
	int n;
	scanf("%d", &n);

	f[0] = 1;
	f[1] = 1;
	for (int i = 2; i <= 116; i++) 
		f[i] = f[i - 1] + f[i - 3];

	printf("%lld", f[n - 1]);

	return 0;
}