#include <stdio.h>
char s[500001];

int main() {
	int N;
	scanf("%d", &N);
	scanf("%s", s);

	int redbox = 0;
	int bluebox = 0;
	int i = 0;
	while (i < N) {
		if (s[i] == 'R') {
			while (s[i] == 'R')
				i++;

			redbox++;
		}
		else if (s[i] == 'B') {
			while (s[i] == 'B')
				i++;

			bluebox++;
		}
	}

	int cnt = 0;
	if (redbox > bluebox)
		cnt = 1 + bluebox;
	else cnt = 1 + redbox;

	printf("%d", cnt);

	return 0;
}