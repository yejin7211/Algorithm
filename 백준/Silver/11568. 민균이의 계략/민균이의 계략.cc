#include <stdio.h>
typedef struct {
	int num;
	int cnt;
}Card;
Card card[1000];

int main() {
	int n;
	scanf("%d", &n);

	int maxCnt = 0;
	for (int i = 0; i < n; i++) {
		scanf("%d", &card[i].num);
		card[i].cnt = 1;
		for (int j = 0; j < i; j++) {
			if (card[j].num < card[i].num && card[i].cnt < card[j].cnt + 1)
				card[i].cnt = card[j].cnt + 1;
		}
		maxCnt = maxCnt > card[i].cnt ? maxCnt : card[i].cnt;
	}

	printf("%d", maxCnt);

	return 0;
}