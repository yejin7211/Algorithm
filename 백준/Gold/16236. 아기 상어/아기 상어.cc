#include <iostream>
#include <cstdbool>
#include <queue>
#include <tuple>

using namespace std;

queue<tuple<int,int,int>> q; // 아기 상어의 y좌표, x좌표, 움직임 횟수
int map[20][20];
bool visited[20][20];
int ypos, xpos, sharkSize = 2, eatenFish = 0; //아기 상어의 위치, 크기, 먹은 물고기 수
int n;

int dy[4] = { -1,1,0,0 };
int dx[4] = { 0,0,-1,1 };

/*
* 먹을 수 있는 물고기의 각각 거리 찾기
* 아기 상어가 가장 가까운 물고기에게 이동
*/

void reset() {
	q = queue<tuple<int, int, int>>();
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			visited[i][j] = false;
}

int bfs(int goal_y, int goal_x) {
	q.push({ ypos,xpos,0 });
	visited[ypos][xpos] = true;

	while (!q.empty()) {
		int y = get<0>(q.front());
		int x = get<1>(q.front());
		int moved = get<2>(q.front());
		q.pop();

		if (y == goal_y && x == goal_x) 
			return moved;

		for (int i = 0; i < 4; i++) {
			int ny = y + dy[i];
			int nx = x + dx[i];

			if (ny < 0 || nx < 0 || ny >= n || nx >= n) continue;		
			//크기가 같은 물고기는 먹을 수 없지만, 해당 칸은 지나갈 수 있다.
			if (!visited[ny][nx] && map[ny][nx] <= sharkSize) {
				q.push({ ny,nx,moved + 1 });
				visited[ny][nx] = true;
			}
		}
	}
	return -1;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	// 입력
	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> map[i][j];
			if (map[i][j] == 9) {
				ypos = i;
				xpos = j;
			}
		}
	}

	int totalT = 0;
	while (1) {
		int minT = 987654321;
		int new_ypos = ypos, new_xpos = xpos;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (map[i][j] != 9 && map[i][j] != 0 && map[i][j] < sharkSize) { //먹을 수 있는 물고기 발견
					int t = bfs(i, j); // 먹을 수 있는 물고기와의 거리 구하기
					if (t!= -1 && minT > t) {
						minT = t; 
						new_ypos = i; 
						new_xpos = j; 
					}
					reset(); 
				}
			}
		}
		
		//더 이상 먹을 수 있는 물고기가 없다면, 엄마 상어에게 도움을 요청한다.
		if (minT == 987654321) 
			break; 
		
		//먹을 수 있는 물고기 중 거리가 가장 가까운 물고기를 먹으러 간다.
		totalT += minT;  
		map[ypos][xpos] = 0;
		ypos = new_ypos;  
		xpos = new_xpos;
		map[ypos][xpos] = 9;
		eatenFish++;

		//아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다.
		if (sharkSize == eatenFish) {
			eatenFish = 0;
			sharkSize++;
		}
	}
	cout << totalT;
	return 0;
}