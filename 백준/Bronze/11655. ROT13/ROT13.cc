#include <stdio.h>
#include <string.h>
char s[101];

int main() {
	scanf("%[^\n]s", s);
	int len = strlen(s);

	int i = 0;
	while (i < len) {
		if ('A' <= s[i] && s[i] <= 'Z') {
			if (s[i] + 13 <= 90) printf("%c", s[i] + 13);
			else printf("%c", s[i] - 13);
		}
		else if ('a' <= s[i] && s[i] <= 'z') {
			if (s[i] + 13 <= 122) printf("%c", s[i] + 13);
			else printf("%c", s[i] - 13);
		}
		else if (s[i] == ' ') printf(" ");
		else if ('0' <= s[i] && s[i] <= '9') printf("%c", s[i]);

		i++;
	}

	return 0;
}