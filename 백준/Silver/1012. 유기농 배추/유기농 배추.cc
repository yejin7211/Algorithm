#include <stdio.h>
#include <stdbool.h>
int map[50][50];
bool visited[50][50];
int m, n, k, cnt = 0;

void init() {
	cnt = 0;
	for (int i = 0; i < 50; i++) {
		for (int j = 0; j < 50; j++) {
			map[i][j] = 0;
			visited[i][j] = false;
		}
	}
}

void input() {
	int a, b;

	scanf("%d %d %d", &m, &n, &k);
	for (int i = 0; i < k; i++) {
		scanf("%d %d", &a, &b);
		map[b][a] = 1;
	}
}

void bfs(int y, int x) {
	int moveX[4] = { 0,0,-1,1 };
	int moveY[4] = { -1,1,0,0 };
	
	visited[y][x] = true;
	int found = 0;
	while (1) {
		found = 0;
		for (int a = 0; a < 4; a++) {
			int xpos = x + moveX[a];
			int ypos = y + moveY[a];

			if (xpos < 0 || m <= xpos || ypos < 0 || n <= ypos || visited[ypos][xpos])
				continue;

			if (!visited[ypos][xpos] && map[ypos][xpos]==1) {
				visited[ypos][xpos] = true;
				found = 1;
				bfs(ypos, xpos);
				break;
			}
		}

		if (found==0)
			break;
	}
}

int main() {
	int t;
	scanf("%d", &t);

	while (t--) {
		init();
		input();
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (map[i][j] == 1 && !visited[i][j]) {
					bfs(i, j);
					cnt++;
				}
			}
		}
		
		printf("%d\n", cnt);
	}

	return 0;
}