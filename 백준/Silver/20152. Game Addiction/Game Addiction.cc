#include <iostream>
#include <cmath>
using namespace std;

int main() {
	int h, n;
	cin >> h >> n;
	
	long long map[31][31] = { 0 };
	for (int j = 0; j < 31; j++) map[0][j] = 1;
	for (int i = 1; i < 31; i++) {
		for (int j = i; j < 31; j++)
			map[i][j] = map[i - 1][j] + map[i][j - 1];
	}

	int k = abs(h - n);
	cout << map[k][k];
	return 0;
}