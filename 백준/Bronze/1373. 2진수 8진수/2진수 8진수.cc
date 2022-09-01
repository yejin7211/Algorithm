#include <stdio.h>
#include <string.h>
char s[1000001];
int arr[1000000];

int main() {
	scanf("%s", s);
	int len = strlen(s);

	int n = 1;
	int count = 0;
	int arrIdx = 0;
	for (int i = len - 1; i >= 0; i--) {
		if (s[i] == '1') 
			arr[arrIdx] += n;

		count++;
		n *= 2;
		if (count == 3) {
			count = 0;
			n = 1;
			arrIdx++;
		}
	}
	if (count > 0)
		arrIdx++;

	if (arrIdx == 0) {
		printf("%d", 0);
		return 0;
	}

	for (int i = arrIdx - 1; i >= 0; i--)
		printf("%d", arr[i]);

	return 0;
}