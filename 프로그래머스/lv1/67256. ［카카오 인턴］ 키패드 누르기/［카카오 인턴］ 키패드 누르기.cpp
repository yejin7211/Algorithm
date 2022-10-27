#include <iostream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

struct keyPos {
    int y;
    int x;
};

keyPos curPos[2] = {
    { 4, 1 },
    { 4, 3 }
};

keyPos numPos[10] = {
            {4, 2},
    {1, 1}, {1, 2}, {1, 3},
    {2, 1}, {2, 2}, {2, 3},
    {3, 1}, {3, 2}, {3, 3}
};

int search_distance(int key, int fingerIdx) {
    return abs(curPos[fingerIdx].y - numPos[key].y) +
        abs(curPos[fingerIdx].x - numPos[key].x);
}

void move_finger(int key, int fingerIdx) {
    curPos[fingerIdx].y = numPos[key].y;
    curPos[fingerIdx].x = numPos[key].x;
}

string solution(vector<int> numbers, string hand) {
    string answer = "";
    
    for (int i = 0; i < numbers.size(); i++) {
        if (numbers[i] == 1 || numbers[i] == 4 || numbers[i] == 7) {
            answer += 'L';
            move_finger(numbers[i], 0);
        }
        else if (numbers[i] == 3 || numbers[i] == 6 || numbers[i] == 9) {
            answer += 'R';
            move_finger(numbers[i], 1);
        }
        else {
            int distance_fromLeftFinger = search_distance(numbers[i], 0);
            int distance_fromRightFinger = search_distance(numbers[i], 1);
            if (distance_fromLeftFinger < distance_fromRightFinger) {
                answer += 'L';
                move_finger(numbers[i], 0);
            }
            else if (distance_fromLeftFinger > distance_fromRightFinger) {
                answer += 'R';
                move_finger(numbers[i], 1);
            }
            else {
                if (hand[0] == 'l') {
                    answer += 'L';
                    move_finger(numbers[i], 0);
                }
                else {
                    answer += 'R';
                    move_finger(numbers[i], 1);
                }
            }
        }
    }
    
    return answer;
}