#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char s[51];
int nums[30];

int main() {
	scanf("%s", s);
	int len = strlen(s);

	int numBegin = -1;
	int nIdx = 0;
	for (int i = 0; i < len; i++) {
		if ('0' <= s[i] && s[i] <= '9') {
			if (numBegin == -1)
				numBegin = i;
		}
		else {
			nums[s[i] == '-' ? nIdx++ : nIdx] += atoi(&s[numBegin]);
			numBegin = -1;
		}
	}
	nums[nIdx++] += atoi(&s[numBegin]);
	int first = nums[0];
	for (int i = 1; i < nIdx; i++)
		first -= nums[i];

	printf("%d", first);

	return 0;
}

//55 50
// 
//0-100+150-50+100 -> -300
//0 250 150