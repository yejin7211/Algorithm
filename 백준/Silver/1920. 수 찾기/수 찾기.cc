#include <stdio.h>
#include <stdlib.h>
int n[100000];
int m[100000];
int N, M;
//
//int compare(const void* a, const void* b) {
//	return *(int*)a - *(int*)b;
//}
void mergeTwoArea(int arr[], int left, int mid, int right) {
	int fIdx = left;
	int rIdx = mid + 1;
	int* sortArr = (int*)malloc(sizeof(int) * N);
	int sIdx = left;
	while (fIdx <= mid && rIdx <= right) {
		if (arr[fIdx] <= arr[rIdx]) sortArr[sIdx++] = arr[fIdx++];
		else sortArr[sIdx++] = arr[rIdx++];
	}
	while (fIdx <= mid) sortArr[sIdx++] = arr[fIdx++];
	while (rIdx <= right) sortArr[sIdx++] = arr[rIdx++];

	for (int i = left; i <= right; i++) arr[i] = sortArr[i];
	free(sortArr);
}

void mergesort(int arr[], int left, int right) {
	if (left < right) {
		int mid = (left + right) / 2;
		mergesort(arr, left, mid);
		mergesort(arr, mid + 1, right);
		mergeTwoArea(arr, left, mid, right);
	}
}
int binarysearch(int start, int end, int target) {
	while (start <= end) {
		int mid = (start + end) / 2;
		if (target == n[mid]) return 1;
		else if (target < n[mid]) end = mid - 1;
		else start = mid + 1;
	}
	return 0;
}
int main() {
	scanf("%d", &N);
	for (int i = 0; i < N; i++)
		scanf("%d", &n[i]);

//	qsort(n, N, sizeof(int), compare);
	mergesort(n, 0, N - 1);

	scanf("%d", &M);
	for (int i = 0; i < M; i++) {
		scanf("%d", &m[i]);
		printf("%d\n", binarysearch(0, N - 1, m[i]));
	}

	return 0;
}