#include <stdio.h>
#include <stdlib.h>
int N, L[21], J[21];
int max_totalJ = 0;

void dfs(int idx, int totalL, int totalJ) {
	if (totalL < 1) return;
	if (idx > N) {
		max_totalJ = max_totalJ > totalJ ? max_totalJ : totalJ;
		return;
	}

	dfs(idx + 1, totalL - L[idx], totalJ + J[idx]);
	dfs(idx + 1, totalL, totalJ);
}

int main() {
	scanf("%d", &N);

	for (int i = 1; i <= N; i++)
		scanf("%d", &L[i]);
	for (int i = 1; i <= N; i++)
		scanf("%d", &J[i]);

	dfs(1, 100, 0);

	printf("%d", max_totalJ);

	return 0;
}