#include <stdio.h>
int N, M;
int map[100][100] = { 0 };
int q[10000][2] = { 0 };

int dx[4] = {-1,1,0,0};
int dy[4] = {0,0,-1,1};

void BFS() {
	int front = 0;
	int rear = 0;
	q[rear][0] = 0; //x인덱스
	q[rear][1] = 0; //y인덱스
	rear++;

	while (front < rear) {
		int xpop = q[front][0];
		int ypop = q[front][1];
		front++;

		for (int i = 0; i < 4; i++) {
			int moveX = xpop + dx[i];
			int moveY = ypop + dy[i];

			if (moveX<0 || moveX>N-1 || moveY<0 || moveY>M-1)
				continue;

			if (map[moveX][moveY] != 1)
				continue;

			map[moveX][moveY] = map[xpop][ypop] + 1;

			q[rear][0] = moveX;
			q[rear][1] = moveY;
			rear++;
		}
	}
}

int main() {
	scanf("%d %d", &N, &M);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++)
			scanf("%1d", &map[i][j]);
	}

	BFS();
	printf("%d\n", map[N-1][M-1]);
	return 0;
}