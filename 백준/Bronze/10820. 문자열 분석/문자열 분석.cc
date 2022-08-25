#include <stdio.h>
#include <string.h>
char s[102];

int main() {
	while (scanf("%[^\n]s",s) != EOF) {
		getchar();
		int len = strlen(s);

		int small = 0;
		int big = 0;
		int num = 0;
		int space = 0;
		for (int i = 0; i < len; i++) {
			if ('A' <= s[i] && s[i] <= 'Z') big++;
			else if ('a' <= s[i] && s[i] <= 'z') small++;
			else if ('0' <= s[i] && s[i] <= '9') num++;
			else if (s[i] == ' ') space++;
		}
		printf("%d %d %d %d\n", small, big, num, space);
	}
	return 0;
}