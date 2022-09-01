#include <stdio.h>
#include <string.h>
char s[333444];

int main() {
	scanf("%s", s);
	int len = strlen(s);

	if (len == 1 && s[0] == '0') {
		printf("0");
		return 0;
	}
	
	int first = 1; //아직 쓰지 않음
	for (int i = 0; i < len; i++) {
		if (s[i] == '7') 
			printf("111");
		else if (s[i] == '6') 
			printf("110");
		else if (s[i] == '5') 
			printf("101");
		else if (s[i] == '4') 
			printf("100");
		else if (s[i] == '3') {
			if (first == 1) printf("11");
			else printf("011");
		}
		else if (s[i] == '2') {
			if (first == 1) printf("10");
			else printf("010");
		}
		else if (s[i] == '1') {
			if (first == 1) printf("1");
			else printf("001");
		}
		else if (s[i] == '0') {
			if (first == 0) printf("000");
		}

		first = 0;
	}

	if (first == 1)
		printf("0");

	return 0;
}