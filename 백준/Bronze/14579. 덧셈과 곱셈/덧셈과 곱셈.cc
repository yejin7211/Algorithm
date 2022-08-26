#include <stdio.h>

int main() {
	int a, b;
	scanf("%d %d", &a, &b);
	
	int sum = 0;
	for (int i = 1; i < a; i++)
		sum += i;

	int ans = 1;
	for (int i = a; i <= b; i++) {
		sum += i;
		ans *= (sum % 14579);
		ans %= 14579;
	}
	
	printf("%d", ans);

	return 0;
}