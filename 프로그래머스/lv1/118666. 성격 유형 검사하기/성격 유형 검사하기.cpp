#include <string>
#include <vector>

using namespace std;

int scores[4];

string solution(vector<string> survey, vector<int> choices) {
    string answer = "";
    
    for(int i = 0; i < choices.size(); i++){
        switch (survey[i][0]) {
            case 'R':
                scores[0] += choices[i] - 4;
                break;
            case 'T':
                scores[0] -= choices[i] - 4;
                break;
            case 'C':
                scores[1] += choices[i] - 4;
                break;
            case 'F':
                scores[1] -= choices[i] - 4;
                break;
            case 'J':
                scores[2] += choices[i] - 4;
                break;
            case 'M':
                scores[2] -= choices[i] - 4;
                break;
            case 'A':
                scores[3] += choices[i] - 4;
                break;
            case 'N':
                scores[3] -= choices[i] - 4;
                break;
        }
    }
    
    if (scores[0] > 0) answer += 'T';
    else answer += 'R';
    
    if (scores[1] <= 0) answer += 'C';
    else answer += 'F';
    
    if (scores[2] <= 0) answer += 'J';
    else answer += 'M';
    
    if (scores[3] <= 0) answer += 'A';
    else answer += 'N';
    
    return answer;
}