#include <stdio.h>
#include <string.h>
char b1[31];
char b2[31];

long long searchNum(char s[31]) {
	int len = strlen(s);

	long long m = 1;
	long long sum = 0;
	for (long long i = len - 1; i >= 0; i--) {
		if (s[i] == '1') 
			sum += m;
		
		m *= 2;
	}

	return sum;
}
int main() {
	scanf("%s", b1);
	scanf("%s", b2);

	long long n1 = searchNum(b1);
	long long n2 = searchNum(b2);
	long long result = n1 * n2;

	long long m = 1;
	long long len = 1;
	while (result >= m) {
		m *= 2;
		len++;
	}
	m /= 2;
	len--;
    
	while (len != 0) {
		if (result >= m) {
			printf("1");
			result -= m;
			m /= 2;
		}
		else {
			printf("0");
			m /= 2;
		}
		len--;
	}

	return 0;
}