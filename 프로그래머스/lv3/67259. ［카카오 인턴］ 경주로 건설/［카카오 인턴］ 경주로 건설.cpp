#include <string>
#include <vector>
#include <queue>
#include <cstring>

using namespace std;

struct Car {
    int y, x, cost, dir;
};

int solution(vector<vector<int>> board) {
    int answer = 987654321;
    
    int dy[4] = {-1,1,0,0};
    int dx[4] = {0,0,-1,1};
    
    int n = board.size();
    int map[n][n][4];  // 방향별 최소 비용
    memset(map, 0, sizeof(map));
    
    queue<Car> q;
    q.push({ 0, 0, 0, -1 });
    while(!q.empty()) {
        int y = q.front().y;
        int x = q.front().x;
        int cost = q.front().cost;
        int dir = q.front().dir;
        q.pop();
        if (y == n-1 && x == n-1) {
            answer = answer < cost ? answer : cost;
            continue;
        }
        for (int i = 0; i < 4; i++) {
            int ny = y + dy[i];
            int nx = x + dx[i];
            if (ny<0 || nx<0 || ny>=n || nx>=n || board[ny][nx]==1) continue;
            int next_cost = cost + 100;
            if (dir!=-1 && dir!=i) next_cost += 500;
            if (map[ny][nx][i] >= next_cost || map[ny][nx][i] == 0) {
                map[ny][nx][i] = next_cost;
                q.push({ ny, nx, next_cost, i });
            }
        }
    }
    return answer;
}