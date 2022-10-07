#include <iostream>
#include <cstdbool>
#include <vector>

using namespace std;

struct Virus {
	int y;
	int x;
	int l;
};
int map[201][201];
vector<Virus> v;
int n, k;

int dy[4] = { -1,1,0,0 };
int dx[4] = { 0,0,-1,1 };

void bfs() {
	int size = v.size();
	for (int i = 0; i < size; i++) {
		for (int k = 0; k < 4; k++) {
			int ny = v[i].y + dy[k];
			int nx = v[i].x + dx[k];
			if (nx <= 0 || ny <= 0 || nx > n || ny > n) continue;
			if (map[ny][nx] == 0) {
				map[ny][nx] = v[i].l;
				v.push_back({ ny,nx,v[i].l });
			}
		}
	}
	v.erase(v.begin(), v.begin() + size);
}

void push_queue(int l) {
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			if (map[i][j] == l)
				v.push_back({ i,j,l });
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n >> k;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			cin >> map[i][j];
		}
	}
	int s, x, y;
	cin >> s >> x >> y;

	for (int i = 1; i <= k; i++)
		push_queue(i);

	while (s--) bfs();
	cout << map[x][y];
	return 0;
}