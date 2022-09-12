#include <stdio.h>
typedef struct {
	int size;
	int cnt;
}Array;

int main() {
	int n;
	scanf("%d", &n);

	Array arr[1000];
	for (int i = 0; i < n; i++){
		scanf("%d", &arr[i].size);
		arr[i].cnt = 1;
	}

	int max = 0;
	for (int i = n - 1; i >= 0; i--) {
		for (int j = i + 1; j < n; j++) {
			if (arr[j].size < arr[i].size && arr[i].cnt < arr[j].cnt + 1)
				arr[i].cnt = arr[j].cnt + 1;
		}
		max = max > arr[i].cnt ? max : arr[i].cnt;
	}

	printf("%d", max);

	return 0;
}