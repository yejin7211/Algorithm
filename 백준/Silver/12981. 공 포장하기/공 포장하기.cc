#include <stdio.h>

int main() {
	int R, G, B;
	scanf("%d %d %d", &R, &G, &B);

	int cnt = 0;
	while (R > 0 && G > 0 && B > 0) {
		cnt++;
		R--;
		G--;
		B--;
	}
//박스에 들어가는 공의 색은 모두 다르거나, 모두 같아야 한다.
	//필요한 박스 개수의 최솟값을 구하는 프로그램을 작성하시오.

	if (R >= 3) {
		cnt += R / 3;
		R %= 3;
	}
	if (G >= 3) {
		cnt += G / 3;
		G %= 3;
	}
	if (B >= 3) {
		cnt += B / 3;
		B %= 3;
	}
	while (R > 0 && G > 0) {
		cnt++;
		R--;
		G--;
	}
	while (R > 0 && B > 0) {
		cnt++;
		R--;
		B--;
	}
	while (G > 0 && B > 0) {
		cnt++;
		G--;
		B--;
	}

	if (R > 0) cnt++;
	if (G > 0) cnt++;
	if (B > 0) cnt++;

	printf("%d", cnt);

	return 0;
}