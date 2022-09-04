#include <stdio.h>
#include <stdlib.h>
#define MAX(a,b) ( (a)>(b)?(a):(b) )
double dp[10001] = { 1 };
void Swap(double arr[], int a, int b) // a,b 스왑 함수 
{
    double temp = arr[a];
    arr[a] = arr[b];
    arr[b] = temp;
}
int Partition(double arr[], int left, int right)
{
    float pivot = arr[left]; // 피벗의 위치는 가장 왼쪽에서 시작
    int low = left + 1;
    int high = right;

    while (low <= high) // 교차되기 전까지 반복한다 
    {
        while (pivot >= arr[low] && low <= right) // 피벗보다 큰 값을 찾는 과정 
        {
            low++; // low를 오른쪽으로 이동 
        }
        while (pivot <= arr[high] && high >= (left + 1)) // 피벗보다 작은 값을 찾는 과정 
        {
            high--; // high를 왼쪽으로 이동
        }
        if (low <= high)// 교차되지 않은 상태이면 스왑 과정 실행 
        {
            Swap(arr, low, high); //low와 high를 스왑 
        }
    }
    Swap(arr, left, high); // 피벗과 high가 가리키는 대상을 교환 
    return high;  // 옮겨진 피벗의 위치정보를 반환 

}


void QuickSort(double arr[], int left, int right)
{
    if (left <= right)
    {
        int pivot = Partition(arr, left, right);   // 둘로 나누어서
        QuickSort(arr, left, pivot - 1);   // 왼쪽 영역을 정렬한다.
        QuickSort(arr, pivot + 1, right);   // 오른쪽 영역을 정렬한다.
    }
}


int main() {
	int N;
	scanf("%d", &N);

	scanf("%lf", &dp[0]);
	double n;
	double max = 0;
	int idx = 0;
	for (int i = 1; i < N; i++) {
		scanf("%lf", &n);
		max = MAX(dp[idx] * n, n);
		if (dp[idx] > max) { //더 이상 이어붙이지 않음
			dp[++idx] = max;
		}
		else dp[idx] = max;
	}

	if (idx == 0) printf("%.3lf", dp[0]);
	else {
		QuickSort(dp, 0, idx - 1);
		printf("%.3lf", dp[idx - 1]);
	}
	
	return 0;
}