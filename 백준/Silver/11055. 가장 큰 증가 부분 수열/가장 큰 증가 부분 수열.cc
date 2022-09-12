#include <stdio.h>
typedef struct {
	int size;
	int total;
	int cnt;
}Array;

int main() {
	int n;
	scanf("%d", &n);
	
	Array arr[1000];
	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i].size);
		arr[i].total = arr[i].size;
		arr[i].cnt = 1;
	}

	int max = 0;
	for (int i = 0; i < n; i++) {
		int max_total = 0;
		for (int j = 0; j < i; j++) {
			if (arr[j].size < arr[i].size && arr[i].cnt < arr[j].cnt + 1) {
				max_total = max_total > arr[j].total ? max_total : arr[j].total;
			}
		}
		arr[i].total = max_total + arr[i].size;
		arr[i].cnt++;
		max = max > arr[i].total ? max : arr[i].total;
	}

	printf("%d", max);

	return 0;
}