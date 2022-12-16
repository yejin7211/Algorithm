#include <iostream>

using namespace std;

int n, k;
int temp[100000];

int slicing_window(){
    int maxSum = -9999;
    int start = 0;
    int curSum = 0;
    for (int end = 0; end < n; end++) {
        curSum += temp[end];
        if (end - start + 1 == k) {
            maxSum = maxSum > curSum ? maxSum : curSum;
            curSum -= temp[start];
            start++;
        }
    }
    return maxSum;
}

int main(){
    cin >> n >> k;
    for (int i = 0; i < n; i++)
        cin >> temp[i];
    
    cout << slicing_window();
    return 0;
}