#include <stdio.h>
#include <stdlib.h>
//minheap 구현
typedef struct {
	long long heap[1001];
	long long cnt;
}Heap;

void heapInit(Heap* h) {
	h->cnt = 0;
}
void swap(long long* a, long long* b) {
	long long tmp = *a;
	*a = *b;
	*b = tmp;
}
void heapPush(Heap* h, long long data) {
	h->heap[++h->cnt] = data;

	long long child = h->cnt;
	long long parent = child / 2;

	while (child != 1 && h->heap[parent] > h->heap[child]) {
		swap(&h->heap[parent], &h->heap[child]);
		child = parent;
		parent = child / 2;
	}
}
long long heapPop(Heap* h) {
	long long ret = h->heap[1];
	swap(&h->heap[1], &h->heap[h->cnt]);
	h->cnt--;

	long long parent = 1;
	long long child = parent * 2;

	if (child + 1 <= h->cnt) {
		if (h->heap[child] > h->heap[child + 1])
			child = child + 1;
	}

	while (child <= h->cnt && h->heap[parent] > h->heap[child]) {
		swap(&h->heap[parent], &h->heap[child]);
		parent = child;
		child = parent * 2;

		if (child + 1 <= h->cnt) {
			if (h->heap[child] > h->heap[child + 1])
				child = child + 1;
		}
	}

	return ret;
}

int compare(const void* a, const void* b) {
	return *(long long*)a - *(long long*)b;
}
int main() {
	long long n, m, a;
	scanf("%lld %lld", &n, &m);

	Heap heap;
	heapInit(&heap);
	for (long long i = 0; i < n; i++) {
		scanf("%lld", &a);
		heapPush(&heap, a);
	}
	
	for (long long i = 0; i < m; i++) {
		long long pop1 = heapPop(&heap);
		long long pop2 = heapPop(&heap);

		heapPush(&heap, pop1 + pop2);
		heapPush(&heap, pop1 + pop2);
	}

	long long sum = 0;
	for (long long i = 0; i < n; i++) 
		sum += heapPop(&heap);

	printf("%lld", sum);

	return 0;
}