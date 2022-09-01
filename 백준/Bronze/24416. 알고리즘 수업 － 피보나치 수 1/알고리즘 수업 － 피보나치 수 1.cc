#include <stdio.h>

int fib(int n) {
	if (n == 1 || n == 2) return 1;
	else return (fib(n - 1) + fib(n - 2));
}
int main() {
	int n;
	scanf("%d", &n);

	int cnt = fib(n);

	printf("%d %d", cnt, n - 2);

	return 0;
}