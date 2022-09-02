#include <stdio.h>
typedef long long ll;
ll t[36];

int main() {
	int n;
	scanf("%d", &n);

	t[0] = 1;

	int i = 0;
	int j = 0;
	for (int m = 1; m <= 35; m++) {
		i = 0;
		j = m - 1;
		for (int k = 0; k < m; k++) {
			t[m] += t[i] * t[j];
			i++;
			j--;
		}
	}

	printf("%lld", t[n]);

	return 0;
}