#include <stdio.h>
#include <stdbool.h>
#include <math.h>
#define MIN(a,b) ( (a)<(b)?(a):(b) )
#define MAX 10000000
bool broken[10];
int n, m;

void input() {
	scanf("%d", &n);
	scanf("%d", &m);

	for (int i = 0; i < m; i++) {
		int x;
		scanf("%d", &x);
		broken[x] = true;
	}
}

int click_from100() {
	return abs(n - 100);
}

bool isPossible(int num) {
	if (num == 0) {
		if (!broken[num]) return true;
		return false;
	}

	while (num) {
		if (broken[num % 10]) return false;
		num /= 10;
	}
	return true;
}

int searchLen(int num) {
	int len = 1;
	while (num / 10 != 0) {
		len++;
		num /= 10;
	}
	return len;
}

int click_fromN() {
	int minClick = MAX;
	for (int i = 0; i <= MAX; i++) {
		if (isPossible(i)) {
			int click = searchLen(i) + abs(i - n);
			minClick = MIN(click, minClick);
		}
	}
	return minClick;
}

int click_minCnt() {
	return MIN(click_from100(), click_fromN());
}

int main() {
	input();
	printf("%d", click_minCnt());
	return 0;
}
