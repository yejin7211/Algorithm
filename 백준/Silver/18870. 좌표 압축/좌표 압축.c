#include <stdio.h>
#include <stdlib.h>
int N;
int X[1000001];
int Y[1000001];
int BinarySearch(int ar[], int n, int target) {
	int low, high;
	int mid;
	low = 0;
	high = n - 1;
	while (low <= high) {
		mid = (low + high) / 2;
		if (target == ar[mid])
			return mid;
		else if (target < ar[mid])
			high = mid - 1;
		else if (target > ar[mid])
			low = mid + 1;
	}
	return -1;
}
int compare(const void* a, const void* b) {
	return *(int*)a - *(int*)b;
}
int Unique(int ar[], int N) {
	int j = 0;
	for (int i = 1; i < N; i++) {
		if (ar[j] == ar[i]) continue;
		ar[++j] = ar[i];
	}
	return ++j;
}
int main() {
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		scanf("%d", &X[i]); // 2 4 -10 4 -9
		Y[i] = X[i];
	}

	qsort(Y, N, sizeof(int), compare);

	int cnt = Unique(Y, N);
	for (int i = 0; i < N; i++)
		printf("%d ",BinarySearch(Y, cnt, X[i]));
	return 0;
}