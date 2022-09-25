#include <stdio.h>
#define MAX	1000
int a[MAX + 1][MAX + 1];
int visited[MAX + 1];
int queue[MAX + 1];
int N, M, V;
void VisitedInit(void) {
	for (int i = 1; i <= N; i++)
		visited[i] = 0;
}
void DFS(int V) {
	printf("%d ", V);
	visited[V] = 1;
	
	for (int i = 1; i <= N; i++) {
		if (a[V][i] == 1 && visited[i] == 0)
			DFS(i);
	}
	return;
}
void BFS(int V) {
	int front = 0;
	int rear = 0;
	int pop;
	
	printf("%d ", V);
	visited[V] = 1;
	queue[0] = V;
	rear++;
	
	while (front < rear) {
		pop = queue[front];
		front++;
		for (int i = 1; i <= N; i++) {
			if (a[pop][i] == 1 && visited[i] == 0) {
				printf("%d ", i);
				visited[i] = 1;
				queue[rear] = i;
				rear++;
			}
		}
	}
	return;
}

int main() {
	int x, y;
	scanf("%d %d %d", &N, &M, &V);
	for (int i = 0; i < M; i++) {
		scanf("%d %d", &x, &y);
		a[x][y] = 1;
		a[y][x] = 1;
	}

	VisitedInit();
	DFS(V);
	printf("\n");
	VisitedInit();
	BFS(V);
	printf("\n");
	return 0;
}