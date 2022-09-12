#include <stdio.h>
typedef struct {
	int size;
	int cnt;
}Box;

int main() {
	int n;
	scanf("%d", &n);

	Box box[1000];
	for (int i = 0; i < n; i++){
		scanf("%d", &box[i].size);
		box[i].cnt = 1;
	}

	int max = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < i; j++) {
			if (box[j].size < box[i].size && box[i].cnt < box[j].cnt + 1)
				box[i].cnt = box[j].cnt + 1;
		}
		max = max > box[i].cnt ? max : box[i].cnt;
	}

	printf("%d", max);

	return 0;
}