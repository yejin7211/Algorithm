#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
typedef struct {
	int x;
	int y;
}Queue;
int box[1000][1000] = { 0 }; //토마토 상자기록
int result[1000][1000] = { 0 }; //이동 횟수
bool visited[1000][1000] = { false }; //방문기록
Queue q[1000000]; // SIZE=1000*1000
int M, N, cnt = 0, f = 0, b = 0;
int needRipe, totalRipe = 0;

int dx[4] = { -1,1,0,0 };
int dy[4] = { 0,0,-1,1 };

void BFS() {
	while (f < b) {
		int popx = q[f].x;
		int popy = q[f].y;
		f++;

		for (int j = 0; j < 4; j++) {
			int nx = popx + dx[j];
			int ny = popy + dy[j];

			if (0 <= nx && nx <= N - 1 && 0 <= ny && ny <= M - 1) {
				if (!visited[nx][ny]) {
					visited[nx][ny] = true;
					result[nx][ny] = result[popx][popy] + 1;

					q[b].x = nx;
					q[b].y = ny;
					b++;

					totalRipe += 1;
					if (totalRipe == needRipe) {
						printf("%d\n", result[nx][ny]);
						exit(0);
					}
				}
			}
		}
	}
}

int main() {
	scanf("%d %d", &M, &N);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			scanf("%d", &box[i][j]);
			if (box[i][j] == 0) cnt++;
			else if (box[i][j] == 1) {
				q[b].x = i;
				q[b].y = j;
				b++;
				visited[i][j] = true;
			}
			else if (box[i][j] == -1)
				visited[i][j] = true;
		}
	}

	if (cnt == 0) {
		printf("0\n");
		return 0;
	}

	needRipe = cnt; //익어야하는 토마토의 개수

	BFS();
	printf("-1\n");
	return 0;
}