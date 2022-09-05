#include <stdio.h>

int main() {
	int N;
	scanf("%d", &N);

	int cnt = 0;
	int num = 2;
	int min = -1, max = -1;
	if (N == 2) min = 1;
	for (int i = 3; i <= N; i++) {
		if (cnt == 2) {
			num++;
			cnt = 0;
		}

		min = num;
		cnt++;
	}

	cnt = 0;
	num = 2;
	if (N == 2) max = 1;
	for (int i = 3; i <= N; i++) {
		if (cnt == 2) num++;
		if (cnt == 3) {
			num++;
			cnt = 0;
		}
		max = num;
		cnt++;
	}

	printf("%d %d", min, max);

	return 0;
}