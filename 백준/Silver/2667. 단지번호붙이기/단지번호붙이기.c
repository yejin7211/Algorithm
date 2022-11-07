#include <stdio.h>
#include <stdlib.h>
int map[26][26];
int visited[26][26];
int cnt[626];
int N;
int idx = 0;

void DFS(int i, int j) {
	visited[i][j] = 1;
	cnt[idx]++;
	if (map[i - 1][j] == 1 && visited[i - 1][j] == 0)
		DFS(i - 1, j);
	if (map[i + 1][j] == 1 && visited[i + 1][j] == 0)
		DFS(i + 1, j);
	if (map[i][j - 1] == 1 && visited[i][j - 1] == 0)
		DFS(i, j - 1);
	if (map[i][j + 1] == 1 && visited[i][j + 1] == 0)
		DFS(i, j + 1);
}

int compare(const void* a, const void* b) {
	return *(int*)a - *(int*)b;
}

int main() {
	scanf("%d", &N);
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++)
			scanf("%1d", &map[i][j]);
	}

	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			if (map[i][j] == 1 && visited[i][j] == 0) {
				DFS(i, j);
				idx++;
			}
		}
	}

	printf("%d\n", idx);
	qsort(cnt, idx, sizeof(int), compare);
	for (int i = 0; i < idx; i++)
		printf("%d\n", cnt[i]);
	return 0;
}