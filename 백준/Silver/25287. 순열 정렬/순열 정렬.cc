#include <stdio.h>
#define MAX(a,b) ( (a)>(b)?(a):(b) )
#define MIN(a,b) ( (a)<(b)?(a):(b) )
int arr[50000];

int main() {
	int T, N;
	scanf("%d", &T);
	
	for (int i = 0; i < T; i++) {
		scanf("%d", &N);

		for (int j = 0; j < N; j++)
			scanf("%d", &arr[j]);

		int possible = 1; //true is default
		for (int j = 0; j < N; j++) {
			int min = MIN(arr[j], N - arr[j] + 1);
			int max = MAX(arr[j], N - arr[j] + 1);

			if (j == 0) arr[j] = min;
			else {
				if (min < arr[j - 1]) {
					if (max < arr[j - 1]) possible = 0;
					else arr[j] = max;
				}
				else arr[j] = min;
			}
		}

		if (possible) printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}

//i를 N-i+1로 바꾼다