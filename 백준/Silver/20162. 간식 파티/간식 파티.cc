#include <stdio.h>
typedef struct {
	int like;
	int total;
}Review;

int main() {
	int n;
	scanf("%d", &n);
	
	Review view[1000];
	for (int i = 0; i < n; i++) {
		scanf("%d", &view[i].like);
		view[i].total = view[i].like;
	}

	int max = 0;
	for (int i = n - 1; i >= 0; i--) {
		int max_total = 0;
		for (int j = i + 1; j < n; j++) {
			if (view[i].like < view[j].like)
				max_total = max_total > view[j].total ? max_total : view[j].total;
		}

		view[i].total += max_total;
		max = max > view[i].total ? max : view[i].total;
	}

	printf("%d", max);

	return 0;
}