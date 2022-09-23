#include <stdio.h>
#include <stdlib.h>
struct Array {
	int num;
	int cnt;
};
Array arr[100];
int map[101][101];
int n, m;

void input() {
	scanf("%d %d", &n, &m);
	
	int a, b;
	//각 경로로 이동하는 단계는 현재로썬 1단게씩
	for (int i = 0; i < m; i++) { 
		scanf("%d %d", &a, &b);
		map[a][b] = 1;
		map[b][a] = 1;
	}
}

void sol() {
	for (int k = 1; k <= n; k++) { //거쳐가는 경로
		for (int i = 1; i <= n; i++) { //시작 지점
			for (int j = 1; j <= n; j++) { //도착 지점
				if (i == j) continue; 
				else if (map[i][k] != 0 && map[k][j] != 0) { //0이 된다면 거쳐갈 수 없다
					if (map[i][j] == 0) map[i][j] = map[i][k] + map[k][j]; //아직 경로수가 정해지지않은 곳
					else if (map[i][k] + map[k][j] < map[i][j]) //더 빠르게 갈 수 있다면 변경
						map[i][j] = map[i][k] + map[k][j];
				}
			}
		}
	}

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++)
			arr[i - 1].cnt += map[i][j];
		arr[i - 1].num = i;
	}
}

int compare(const void* a, const void* b) {
	Array* pA = (Array*)a;
	Array* pB = (Array*)b;

	if (pA->cnt == pB->cnt) return pA->num - pB->num;
	return pA->cnt - pB->cnt;
}

int main() {
	input();
	sol();

	qsort(arr, n, sizeof(Array), compare);
	printf("%d", arr[0].num);

	return 0;
}