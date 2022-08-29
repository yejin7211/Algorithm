#include <stdio.h>
#define MIN(a,b) ( (a)<(b)?(a):(b) )

long long func(int n, int x) {
	long long num = 0;
	for (long long i = x; n / i >= 1; i *= x)
		num += n / i;
	return num;
}
int main() {
	int n, m;
	scanf("%d %d", &n, &m);

	long long five = func(n, 5) - func(n - m, 5) - func(m, 5);
	long long two = func(n, 2) - func(n - m, 2) - func(m, 2);

	printf("%lld", MIN(five, two));

	return 0;
}