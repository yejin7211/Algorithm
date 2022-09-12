#include <stdio.h>
typedef struct {
	int size;
	int cnt;
}Box;
Box box[5000];

int main() {
	int n;
	scanf("%d", &n);

	int max = 0;
	for (int i = 0; i < n; i++) {
		scanf("%d", &box[i].size);
		box[i].cnt = 1;
	
		int maxCnt = 0;
		for (int j = 0; j < i; j++) {
			if (box[j].size < box[i].size)
				maxCnt = maxCnt > box[j].cnt ? maxCnt : box[j].cnt;
		}
		box[i].cnt += maxCnt;
		max = max > box[i].cnt ? max : box[i].cnt;
	}

	printf("%d", max);

	return 0;
}