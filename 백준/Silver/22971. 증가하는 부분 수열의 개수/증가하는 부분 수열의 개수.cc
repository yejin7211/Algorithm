#include <stdio.h>
typedef struct {
	int a;
	int cnt;
}Array;
Array arr[5000];

int main() {
	int n;
	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i].a);
		arr[i].cnt = 1;
		for (int j = 0; j < i; j++) {
			if (arr[j].a < arr[i].a) {
				arr[i].cnt += arr[j].cnt;
				arr[i].cnt %= 998244353;
			}
		}
		printf("%d ", arr[i].cnt);
	}

	return 0;
}