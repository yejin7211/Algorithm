#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> scoville, int K) {
    priority_queue<int, vector<int>, greater<int>> pq;
    for (int i = 0; i < scoville.size(); i++)
        pq.push(scoville[i]);

    int cnt = 0;
    while(1) {
        if (pq.size() < 2 || pq.top() >= K)
            break;
        int n1 = pq.top();
        pq.pop();
        int n2 = pq.top();
        pq.pop();
        pq.push(n1 + n2 * 2);
        cnt++;
    }
    if (pq.top() >= K) 
        return cnt;
    return -1;
}