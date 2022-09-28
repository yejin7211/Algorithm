#include <iostream>
#include <cstdbool>
#include <cmath>
using namespace std;
int map[2188][2188];
int negativeNum = 0;
int zeroNum = 0;
int positiveNum = 0;

void countNum(int num) {
	switch (num) {
	case -1:
		negativeNum++;
		break;
	case 0:
		zeroNum++;
		break;
	case 1:
		positiveNum++;
		break;
	default:
		break;
	}
}

bool isAllSame(int row, int col, int len) {
	for (int i = row; i < row + len; i++) {
		for (int j = col; j < col + len; j++) {
			if (map[i][j] != map[row][col]) return false;
		}
	}
	return true;
}

void divideArea(int rowIdx, int colIdx, int len) {
	int totalBlocks = len * len;
	int newLen = sqrt(totalBlocks / 9);
	//cout << rowIdx << " " << colIdx << " " << len << '\n';
    
	for (int i = rowIdx; i < rowIdx + len; i++) {
		for (int j = colIdx; j < colIdx + len; j++) {
			if ((i == rowIdx || i == rowIdx + newLen || i == rowIdx + newLen * 2) &&
				(j == colIdx || j == colIdx + newLen || j == colIdx + newLen * 2)) {
				if (isAllSame(i, j, newLen)) countNum(map[i][j]);
				else divideArea(i, j, newLen);
			}
		}
	}
}
int main() {
    ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n;
	cin >> n;

	int allSame = 1;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> map[i][j];
			if (map[i][j] != map[0][0])
				allSame = 0;
		}
	}

	if (allSame == 1) countNum(map[0][0]);
	else divideArea(0, 0, n);

	cout << negativeNum << '\n';
	cout << zeroNum << '\n';
	cout << positiveNum;
	return 0;
}