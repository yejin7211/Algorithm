#include <stdio.h>
typedef struct {
	int power;
	int cnt;
}Soldier;
Soldier man[2000];

int main() {
	int n;
	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		scanf("%d", &man[i].power);
		man[i].cnt = 1;
	}

	int maxCnt = 0;
	for (int i = n - 1; i >= 0; i--) {
		for (int j = i + 1; j < n; j++) {
			if (man[i].power > man[j].power && man[i].cnt < man[j].cnt + 1)
				man[i].cnt = man[j].cnt + 1;
		}
		
		maxCnt = maxCnt > man[i].cnt ? maxCnt : man[i].cnt;
	}

	printf("%d", n - maxCnt);

	return 0;
}