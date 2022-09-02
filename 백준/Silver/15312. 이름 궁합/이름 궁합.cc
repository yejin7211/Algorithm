#include <stdio.h>
#include <string.h>
char A[2001];
char B[2001];
int dp[4001];
int alpa [26] = {3, 2, 1, 2, 3, 3, 2, 3,
	3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1 };

int main() {
	scanf("%s", A);
	scanf("%s", B);
	int len = strlen(A);

	int idx = 0;
	for (int i = 0; i < len; i++) {
		char a = A[i];
		char b = B[i];

		dp[idx++] = alpa[a - 'A'];
		dp[idx++] = alpa[b - 'A'];
	}

	int totalLen = len * 2; //6
	while (totalLen > 2) {
		for (int i = 0; i < totalLen - 1; i++) 
			dp[i] = (dp[i] + dp[i + 1]) % 10;
			
		totalLen--;
	}

	printf("%d", dp[0]);
	printf("%d", dp[1]);

	return 0;
}