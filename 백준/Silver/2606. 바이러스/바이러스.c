#include <stdio.h>
int map[101][101];
int visited[101];
int cnt = 0;
int com, line, x, y;
void DFS(int c) {
	cnt++;
	visited[c] = 1;

	for (int i = 1; i <= com; i++) {
		if (map[c][i] == 1 && visited[i] == 0)
			DFS(i);
	}
	return;
}
int main() {
	scanf("%d", &com);
	scanf("%d", &line);
	for (int i = 0; i < line; i++) {
		scanf("%d %d", &x, &y);
		map[x][y] = 1;
		map[y][x] = 1;
	}

	for (int i = 1; i <= com; i++)
		visited[i] = 0;
	DFS(1);
	printf("%d\n", cnt-1);
	return 0;
}