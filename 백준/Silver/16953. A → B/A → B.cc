#include <stdio.h>

int searchLen(int n) {
	int len = 1;
	while (n / 10 != 0) {
		n /= 10;
		len *= 10;
	}
	return len;
}
int main() {
	int a, b;
	scanf("%d %d", &a, &b);

	int cnt = 1;
	while (b != a) {
		if (b % 2 == 0) b /= 2;
		else {
			int len = searchLen(b);
			
			int sum = 0;
			while (b / 10 != 0) {
				sum += (b / len) * (len / 10);
				b %= len;
				len /= 10;
			}
			if (b != 1) {
				printf("-1");
				return 0;
			}
			b = sum;
		}

		cnt++;
		if (b < a) {
			printf("-1");
			return 0;
		}
	}

	printf("%d", cnt);

	return 0;
}