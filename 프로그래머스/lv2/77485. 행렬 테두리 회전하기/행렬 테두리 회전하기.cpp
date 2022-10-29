#include <string>
#include <vector>
#define MIN(a,b) ( (a)<(b)?(a):(b) )

using namespace std;

int map[101][101];

void swap(int* a, int* b) {
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

void resetMap(int r, int c) {
    int n = 1;
    for (int i = 1; i <= r; i++) 
        for (int j = 1; j <= c; j++)
            map[i][j] = n++;
}

vector<int> solution(int row, int col, vector<vector<int>> queries) {
    vector<int> answer;
    resetMap(row, col);
    for (int k = 0; k < queries.size(); k++) {
        int y1 = queries[k][0], x1 = queries[k][1];
        int y2 = queries[k][2], x2 = queries[k][3];
        int minNum = map[y1][x1];    
        int tmp = map[y1][x1];
        for (int j = x1 + 1; j <= x2; j++) {
            minNum = MIN(minNum, map[y1][j]);
            swap(&tmp, &map[y1][j]);
        }
        for (int i = y1 + 1; i <= y2; i++) {
            minNum = MIN(minNum, map[i][x2]);
            swap(&tmp, &map[i][x2]);
        }
        for (int j = x2 - 1; j >= x1; j--) {
            minNum = MIN(minNum, map[y2][j]);
            swap(&tmp, &map[y2][j]);
        }
        for (int i = y2 - 1; i >= y1; i--) {
            minNum = MIN(minNum, map[i][x1]);
            swap(&tmp, &map[i][x1]);
        }            
        answer.push_back(minNum);
    }
    
    return answer;
}